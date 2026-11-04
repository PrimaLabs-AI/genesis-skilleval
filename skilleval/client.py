"""Minimal OpenAI-compatible chat client for the PrimaLabs endpoint (stdlib only)."""
from __future__ import annotations

import json
import os
import time
import urllib.error
import urllib.request
from pathlib import Path

LIGHTNING = "primalabs-ai/Nemotron-3.5-Lightning-NVFP4"
DEEPSEEK = "primalabs-ai/DeepSeek-V4.1-Flash-1017"


def _load_env() -> dict:
    env = dict(os.environ)
    dotenv = Path(__file__).resolve().parent.parent / ".env"
    if dotenv.exists():
        for line in dotenv.read_text().splitlines():
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, _, v = line.partition("=")
                env.setdefault(k.strip(), v.strip())
    return env


_ENV = _load_env()


def _provider(model: str):
    """Route by model id: primalabs-ai/* -> PrimaLabs, everything else -> OpenRouter."""
    if model.startswith("primalabs-ai/"):
        return _ENV["PRIMALABS_BASE_URL"].rstrip("/"), _ENV["PRIMALABS_API_KEY"]
    key = _ENV.get("OPENROUTER_API_KEY")
    if not key:
        raise RuntimeError("OPENROUTER_API_KEY not set in .env (needed for non-PrimaLabs models)")
    return "https://openrouter.ai/api/v1", key


def _cli_chat(model: str, messages, retries=3):
    """Subscription-billed backends via local CLIs.

    model = "cli/codex/<model>" (ChatGPT subscription) or "cli/claude/<model>"
    (Claude subscription; requires `claude login`). The CLIs are agent
    harnesses, not raw APIs: results are harness-level comparisons.
    """
    import subprocess
    import tempfile

    _, backend, name = model.split("/", 2)
    system = "\n\n".join(m["content"] for m in messages if m["role"] == "system")
    user = "\n\n".join(m["content"] for m in messages if m["role"] == "user")
    for attempt in range(retries):
        if backend == "codex":
            with tempfile.NamedTemporaryFile(mode="r", suffix=".txt") as out:
                proc = subprocess.run(
                    ["codex", "exec", "--skip-git-repo-check", "--sandbox", "read-only",
                     "-m", name, "--output-last-message", out.name,
                     f"{system}\n\n<user_request>\n{user}\n</user_request>"],
                    capture_output=True, text=True, timeout=600,
                )
                reply = out.read().strip()
        elif backend == "claude":
            proc = subprocess.run(
                ["claude", "-p", "--model", name, "--strict-mcp-config",
                 "--disallowedTools", "*", "--system-prompt", system, user],
                capture_output=True, text=True, timeout=600,
            )
            reply = proc.stdout.strip()
        else:
            raise ValueError(f"unknown cli backend: {backend}")
        if reply:
            return reply
        time.sleep(5 * (attempt + 1))
    raise RuntimeError(f"{backend} cli empty after {retries} tries: {proc.stderr[-300:]}")


def chat(messages, model=LIGHTNING, temperature=0.0, max_tokens=2048, retries=6):
    if model.startswith("cli/"):
        return _cli_chat(model, messages)
    if model.startswith("anthropic/"):
        # OpenRouter passes Anthropic cache_control through: mark the (large,
        # identical-across-calls) system block as cacheable. OpenAI/Gemini
        # cache repeated prefixes automatically.
        messages = [
            {
                "role": m["role"],
                "content": [
                    {"type": "text", "text": m["content"], "cache_control": {"type": "ephemeral"}}
                ],
            }
            if m["role"] == "system"
            else m
            for m in messages
        ]
    payload = {
        "model": model,
        "messages": messages,
        "temperature": temperature,
        "max_tokens": max_tokens,
    }
    base_url, api_key = _provider(model)
    req = urllib.request.Request(
        f"{base_url}/chat/completions",
        data=json.dumps(payload).encode(),
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
    )
    last_err = None
    for attempt in range(retries):
        try:
            with urllib.request.urlopen(req, timeout=300) as resp:
                body = json.load(resp)
            msg = body["choices"][0]["message"]
            content = msg.get("content") or msg.get("reasoning_content") or ""
            # strip <think> blocks if the server inlines reasoning
            if "</think>" in content:
                content = content.rsplit("</think>", 1)[1]
            return content
        except urllib.error.HTTPError as e:
            last_err = e
            if e.code == 429:
                time.sleep(min(15 * (attempt + 1), 60))
            else:
                time.sleep(2**attempt)
        except (OSError, KeyError, json.JSONDecodeError) as e:
            last_err = e
            time.sleep(2**attempt)
    raise RuntimeError(f"chat failed after {retries} retries: {last_err}")


def extract_json(text: str):
    """Pull the first JSON object out of a model reply (tolerates fences/prose)."""
    depth, start = 0, None
    for i, ch in enumerate(text):
        if ch == "{":
            if depth == 0:
                start = i
            depth += 1
        elif ch == "}" and depth:
            depth -= 1
            if depth == 0:
                try:
                    return json.loads(text[start : i + 1])
                except json.JSONDecodeError:
                    start = None
    raise ValueError(f"no JSON object in reply: {text[:200]!r}")
