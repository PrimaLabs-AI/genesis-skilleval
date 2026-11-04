# genesis-skilleval

Routing and compliance benchmark for [Genesis Agent Skills](https://gitlab.osti.gov/genesis/genesis-skills) (DOE Genesis Mission / ModCon) across open and closed models.

**Headline:** on the 36-skill Genesis catalog, NVIDIA's open-weight Nemotron 3.5 Super VL achieves the highest exact-match skill routing of nine models measured — above GPT-5.2, Claude Opus 5.5, Claude Sonnet 5.5, and Gemini 3.5 Flash — on both PrimaLabs serving (0.830) and neutral third-party serving (0.753). Full results and findings: [`report.md`](report.md). Partner brief: [`one-pager.md`](one-pager.md).

## What it measures

Given a scientist's natural-language request and the skill catalog, does the model activate **exactly** the right skill?

- **Activation eval** (`skilleval/run_eval.py`): 120 labeled tasks (108 skill-requiring + 12 distractors), scored on recall, exact-match, precision, and false-activation. Three catalog-loading conditions:
  - `disclosure` — spec-standard progressive disclosure (name+description only, ~3.7k tokens)
  - `preload` — all 36 full SKILL.md bodies in context (~63k tokens)
  - `preload-anchor` — preload + a one-line output-format reminder
- **Execution eval** (`skilleval/exec_eval.py`): model performs the task with the required skill in context; an LLM judge scores adherence/correctness/completeness against the skill's own instructions. Chat-only (no tool loop) — treat as a lower bound.

## Key findings

1. Full-catalog **preload beats progressive disclosure for all 9 models** (+11–18pp exact-match).
2. **Serving affects routing accuracy**, not just speed: the same Super VL checkpoint scores 0.830 (PrimaLabs NVFP4) vs 0.753 (aggregator).
3. **Cross-vendor protocol failure under instruction mass:** mid-capacity models (Nemotron Lightning, GPT-5.2) break the routing output contract on off-catalog tasks under preload (up to 44% of distractors); a one-line anchor eliminates it.
4. **Catalog bugs:** near-duplicate skills cause systematic confusions (`pbs`→`slurm`, `ai-fingerprint`→`fingerprinting`, `i2-api`→`amsc-mag`).

## Setup

```bash
git clone <this repo> && cd gm-agent
git clone https://gitlab.osti.gov/genesis/genesis-skills.git   # skill catalog (not vendored)
cp .env.example .env                                           # fill in keys
```

`.env` keys: `PRIMALABS_BASE_URL`, `PRIMALABS_API_KEY` (PrimaLabs endpoint), `OPENROUTER_API_KEY` (closed-model baselines). Python 3.9+, stdlib only.

## Run

```bash
python3 skilleval/gen_tasks.py                                   # regenerate task set (DeepSeek as generator)
python3 skilleval/run_eval.py --model <model-id> --condition all --trials 3 --resume
python3 skilleval/exec_eval.py --model <model-id>                # execution pilot
python3 skilleval/analyze.py > results/analysis.md               # aggregate tables
```

Model ids: `primalabs-ai/*` → PrimaLabs endpoint; anything else → OpenRouter; `cli/claude/<model>` / `cli/codex/<model>` → local subscription CLIs (harness-level numbers, labeled as such).

## Repo map

| path | contents |
|---|---|
| `skilleval/` | catalog parser, multi-provider client, task generator, activation + execution evals, analysis |
| `tasks/tasks.jsonl` | 120 labeled tasks |
| `results/` | raw per-trial results (all models), aggregate tables |
| `report.md` | full writeup: methods, results, findings, caveats, next steps |
| `one-pager.md` | partner brief (NVIDIA / SRNL) |
| `bug-supervl-tool-tag-loop.md` | serving bug report with deterministic repro |

## Caveats

Synthetic task set (DeepSeek-generated; human audit pending), single-label ground truth, execution eval is chat-only, OpenRouter provider not pinned for the replication run. See `report.md` for the full list.
