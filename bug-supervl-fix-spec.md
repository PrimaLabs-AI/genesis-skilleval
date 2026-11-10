# Super VL no-tools chat: tool-envelope loop — fix spec

**Endpoint:** `primalabs-ai/Nemotron-3.5-Super-VL-NVFP4` (serverless).
**Status 2026-11-09 (later):** ✅ **RESOLVED** — stop-sequence patch deployed and verified; all four acceptance tests pass (AT1 clean stop/0 loops/325 tok; AT2 tools-mode unchanged; AT3 exec scores up to 3.58/3.75/3.00 from 2.78-completeness baseline; AT4 zero `<|open|>`). Residual: 2/36 exec cases show a *text-level* sentence-repetition variant that stop sequences cannot catch — keep/extend the sampler n-gram repetition guard. Earlier same-day status: guard-only mitigation (~15 reps, wrong `finish_reason: length`), root cause then unfixed.
**Lightning is unaffected** (truncates, never loops) — diff the two deployments' configs first; the divergence is probably the whole bug.
Companion report with deterministic repro: [`bug-supervl-tool-tag-loop.md`](bug-supervl-tool-tag-loop.md).

## Observed behavior (repro: 3 s, temp 0, deterministic)

| request shape | result |
|---|---|
| long system prompt (~1.4k tok), **no `tools`** | model emits one valid `<function_calls>…</function_calls>` block, then greedy decode collapses onto the closing tag. Pre-guard: 348 reps to `max_tokens`. Post-guard (today): ~15 reps, stops at 351 completion tokens, **`finish_reason: "length"`** — wrong, no token limit was hit |
| same prompt **with `tools` defined** | clean: 1 structured `tool_calls` entry, `finish_reason: "tool_calls"`, zero loop |
| short system prompt, no tools | no tool attempt, clean stop |
| additional failure variants (seen across exec-eval runs) | `<|open|>argument key=…` pseudo-markup; repeated `</system>`; repeated `</parameter>`; endless `\n` |

## Root-cause hypothesis

Tool-call parsing/stop handling is only active when the request defines `tools`. In no-tools mode the model can still emit its native tool-call envelope (long instruction-style system prompts elicit it), and nothing registers the envelope terminator as a stop sequence — after the closing tag the next-token distribution has no valid continuation, and greedy decoding loops on it. The `<|open|>` variant additionally suggests the deployed chat template may not match NVIDIA's reference for Super VL; the Lightning deployment (same stack, no loop) is the natural diff target.

## Fix, in order of correctness

1. **Stop sequences in no-tools mode.** When the request has no `tools`, add the model's tool-envelope terminator sequence(s) to the sampler stop list — at minimum whatever `</function_calls>` tokenizes to, plus any special tokens the template uses to close a tool block (check the tokenizer: this may be a dedicated special token, not plain text). Generation then stops cleanly after the first complete envelope.
2. **Template audit.** Diff the deployed Super VL chat template (vLLM `--chat-template` / `tokenizer_config.chat_template`) against NVIDIA's reference in the Nemotron 3.5 Super VL HF repo, and against the Lightning deployment. Inspect: tool-section conditionals (`{%- if tools %}`), the generation-prompt suffix, and whether eos / tool-close specials appear in `stop_token_ids`.
3. **`finish_reason` correctness.** Map guard-triggered aborts to `stop` (or a custom reason), never `length` — clients key retry/continuation behavior on this field.
4. **Keep the repetition guard** as a backstop. Optionally strip trailing repeated closing tags from `content` when it fires.

## Acceptance tests

1. Repro script returns `finish_reason: "stop"`, `content.count("</function_calls>") <= 1`, completion tokens ≪ `max_tokens`.
2. With `tools` defined: behavior unchanged (`tool_calls`, no regression).
3. `python3 skilleval/exec_eval.py --model primalabs-ai/Nemotron-3.5-Super-VL-NVFP4` — completeness should rise from the guard-only baseline of **2.78** (measured 2026-11-09; scores were 3.22 adherence / 3.39 correctness / 2.78 completeness, statistically unchanged from pre-guard). Sentinel skills: `battleprint`, `ai-fingerprint`, `agentic-vulnerabilities-scan`, `well-convert`, `amsc-python-client`.
4. The `<|open|>` variant is gone: grep fresh exec results for `<|open|>` — zero occurrences.

## Impact

- Pre-guard, every affected response burned the full completion budget; post-guard it still pollutes agentic pipelines with garbage tags and a wrong finish_reason.
- Artificial Analysis's multi-turn agentic workload exercises exactly this path — plausibly costs Super VL leaderboard position.
- The failure is publicly reproducible: the repro ships in the public genesis-skilleval repo.
