# Bug: Super VL degenerates into repeated tool-call closing tags in plain chat mode

**Model:** `primalabs-ai/Nemotron-3.5-Super-VL-NVFP4` (serverless endpoint)
**Found by:** skill-execution eval in `gm-agent` (2026-11-05). Not reproducible on Lightning (it truncates but does not loop).

## Symptom

When a chat completion (no `tools` in the request) carries an instruction-heavy system prompt that leads the model to emit tool-call syntax, generation collapses into an unbounded repetition of closing tags until `max_tokens`:

```
…</function_calls>
</function_calls>
</function_calls>        <- repeated 348x in the repro below
```

Variants observed: repeated `</function_calls>`, repeated empty `</system>` tags, repeated `</parameter>`, or endless `\n`. Always `finish_reason: "length"` — the full completion budget is consumed by garbage. Prompt caching is unaffected (`cached_tokens` normal).

## Deterministic repro (temp 0, ~1.5k prompt tokens, 3 s)

From `gm-agent/` (uses `.env` creds; skill body from the genesis-skills catalog):

```bash
cd skilleval && python3 - <<'EOF'
import json, sys, urllib.request
sys.path.insert(0, '.')
from catalog import load_catalog
from client import BASE_URL, API_KEY
from exec_eval import EXEC_SYSTEM
s = {x.name: x for x in load_catalog()}['configuration-tester']
task = "Verify that the generated configurations in ./configs run end to end."
payload = {"model": "primalabs-ai/Nemotron-3.5-Super-VL-NVFP4", "temperature": 0, "max_tokens": 2000,
  "messages": [{"role": "system", "content": EXEC_SYSTEM.format(name=s.name, body=s.body)},
               {"role": "user", "content": task}]}
req = urllib.request.Request(BASE_URL + "/chat/completions", data=json.dumps(payload).encode(),
  headers={"Authorization": "Bearer " + API_KEY, "Content-Type": "application/json"})
r = json.load(urllib.request.urlopen(req, timeout=300))
c = r["choices"][0]; m = c["message"]["content"]
print(c["finish_reason"], r["usage"])
print("loop count:", m.count("</function_calls>"))
EOF
```

Observed: `finish_reason=length`, `completion_tokens=2000` (209 reasoning), **348× `</function_calls>`**.

Key detail: a short system prompt does NOT trigger it — the model declines tool use politely. The trigger is a long workflow-style system prompt (full SKILL.md body, ~1.4k tokens) that makes the model start a native tool call despite no `tools` being defined.

## Suspected cause

The model emits its native tool-call envelope; in non-tool chat mode the serving path neither parses it nor treats the envelope terminator as a stop sequence. At temperature 0 the post-envelope distribution collapses onto the closing tag and greedy decoding loops.

## Suggested fixes (any of)

1. Register the tool-call envelope terminators as stop sequences when the request defines no `tools` (mirror whatever the NeMo chat template does for Super VL).
2. Verify the deployed chat template matches NVIDIA's reference template for Super VL — Lightning (same stack) only truncates, suggesting a template/stop-config difference between the two deployments.
3. Backstop: n-gram repetition guard at the sampler for greedy decode.

## Evidence files

- `results/nemotron-3.5-super-vl-nvfp4.exec.jsonl` — 5 affected responses (`amsc-python-client-0`, `datacard-generator-0`, `configuration-implementor-0`, `configuration-tester-0`, `data-exploration-0`) with excerpts.
- Repro above is self-contained given repo + `.env`.