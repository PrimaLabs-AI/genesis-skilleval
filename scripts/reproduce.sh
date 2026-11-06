#!/usr/bin/env bash
# Reproduce the genesis-skilleval benchmark.
#
# Requirements: python3 (3.9+, stdlib only), git, .env with keys (see .env.example).
# Full run costs ~$60 via OpenRouter + PrimaLabs usage. Set SMOKE=1 for a
# free-ish 8-task sanity pass on one model.
set -euo pipefail
cd "$(dirname "$0")/.."

CATALOG_COMMIT=70dce5aca946e2804f9b8579da01910cd2861858

# 1. Pin the skill catalog to the evaluated version.
if [ ! -d genesis-skills ]; then
  git clone https://gitlab.osti.gov/genesis/genesis-skills.git
fi
git -C genesis-skills fetch -q origin && git -C genesis-skills checkout -q "$CATALOG_COMMIT"
echo "catalog pinned to $CATALOG_COMMIT"

# 2. Sanity-check catalog parsing (expect 36 skills).
python3 -c "
import sys; sys.path.insert(0, 'skilleval')
from catalog import load_catalog
n = len(load_catalog())
assert n == 36, f'expected 36 skills, parsed {n}'
print(f'catalog parse ok: {n} skills')"
if [ "${SMOKE:-0}" = "1" ]; then
  echo "== smoke: 8 tasks, disclosure only, Nemotron Lightning =="
  python3 skilleval/run_eval.py --model primalabs-ai/Nemotron-3.5-Lightning-NVFP4 \
    --condition disclosure --trials 1 --limit 8 --workers 2
  exit 0
fi

# 3. Activation eval. Uses the COMMITTED task set (tasks/tasks.jsonl); do not
#    regenerate tasks if you want comparable numbers.
OPEN_MODELS=(
  primalabs-ai/Nemotron-3.5-Lightning-NVFP4
  primalabs-ai/Nemotron-3.5-Super-VL-NVFP4
  primalabs-ai/GLM-5.3-Flash
  primalabs-ai/MiMo-V2.6-Pro
)
ROUTER_MODELS=(
  nvidia/nemotron-3.5-super-vl
  nvidia/nemotron-3.5-lightning
  openai/gpt-5.2
  anthropic/claude-sonnet-5.5
  google/gemini-3.5-flash
)
for m in "${OPEN_MODELS[@]}" "${ROUTER_MODELS[@]}"; do
  python3 skilleval/run_eval.py --model "$m" --condition all --trials 3 --workers 3 --resume
done
# Opus: best-expected config only (cost control).
python3 skilleval/run_eval.py --model anthropic/claude-opus-5.5 --condition preload --trials 3 --workers 3 --resume

# 4. Execution pilot (LLM-judged, chat-only; judge = GLM-5.3-Flash).
python3 skilleval/exec_eval.py --model primalabs-ai/Nemotron-3.5-Lightning-NVFP4 --workers 4
python3 skilleval/exec_eval.py --model primalabs-ai/Nemotron-3.5-Super-VL-NVFP4 --workers 4
python3 skilleval/exec_eval.py --model primalabs-ai/GLM-5.3-Flash --workers 4

# 5. Aggregate tables.
python3 skilleval/analyze.py > results/analysis.md
echo "done -> results/analysis.md"
