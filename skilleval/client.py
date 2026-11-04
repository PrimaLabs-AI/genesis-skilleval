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
BASE_URL = _ENV["PRIMALABS_BASE_URL"].rstrip("/")
API_KEY = _ENV["PRIMALABS_API_KEY"]


def chat(messages, model=LIGHTNING, temperature=0.0, max_tokens=2048, retries=6):
    payload = {
        "model": model,
        "messages": messages,
        "temperature": temperature,
        "max_tokens": max_tokens,
    }
    req = urllib.request.Request(
        f"{BASE_URL}/chat/completions",
        data=json.dumps(payload).encode(),
        headers={
            "Authorization": f"Bearer {API_KEY}",
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
        except (urllib.error.URLError, KeyError, json.JSONDecodeError) as e:
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
