# genesis-skilleval

Routing and compliance benchmark for [Genesis Agent Skills](https://gitlab.osti.gov/genesis/genesis-skills) (DOE Genesis Mission / ModCon) across open and closed models.

**Headline:** on the 36-skill Genesis catalog, NVIDIA's open-weight Nemotron 3.5 Super VL achieves the highest exact-match skill routing of nine models measured — above GPT-5.2, Claude Opus 5.5, Claude Sonnet 5.5, and Gemini 3.5 Flash — on both PrimaLabs serving (0.830) and neutral third-party serving (0.753).

- Full methods, results, findings, caveats: [`report.md`](report.md)
- Partner brief: [`one-pager.md`](one-pager.md) · Broad-audience brief: [`brief-genesis-science-agents.md`](brief-genesis-science-agents.md)
- Serving bug found during the study: [`bug-supervl-tool-tag-loop.md`](bug-supervl-tool-tag-loop.md)

## Results (exact-match, best config per model, mean of 3 trials, temp 0)

| model | serving | exact | recall |
|---|---|---|---|
| Nemotron 3.5 Super VL (open) | PrimaLabs NVFP4 | **0.830** | 0.981 |
| Nemotron 3.5 Super VL (open) | OpenRouter | **0.753** | 0.938 |
| Nemotron 3.5 Lightning (open) | PrimaLabs NVFP4 | 0.738 | 0.855 |
| GPT-5.2 | OpenRouter | 0.716 | 0.947 |
| Nemotron 3.5 Lightning (open) | OpenRouter | 0.707 | 0.827 |
| Claude Opus 5.5 | OpenRouter | 0.679 | 0.997 |
| Gemini 3.5 Flash | OpenRouter | 0.663 | 0.978 |
| GLM-5.3-Flash (open) | PrimaLabs | 0.657 | 0.991 |
| Claude Sonnet 5.5 | OpenRouter | 0.639 | 0.994 |
| MiMo-V2.6-Pro (open) | PrimaLabs | 0.543 | 1.000 |

## What it measures

Given a scientist's natural-language request and the skill catalog, does the model activate **exactly** the right skill?

- **Activation eval** (`skilleval/run_eval.py`): 120 labeled tasks (108 skill-requiring + 12 distractors). Metrics: recall (required skill among selected), exact-match (selected precisely the required skill), precision, false-activation rate on distractors. Three catalog-loading conditions:
  - `disclosure` — spec-standard progressive disclosure (name + description only, ~3.7k tokens)
  - `preload` — all 36 full SKILL.md bodies in context (~63k tokens, cacheable)
  - `preload-anchor` — preload + a one-line output-format reminder appended to the user turn
- **Execution eval** (`skilleval/exec_eval.py`): the model performs one task per skill with the required SKILL.md in context; GLM-5.3-Flash judges adherence/correctness/completeness (1–5) against the skill's own instructions. Chat-only (no tool loop) — treat scores as a lower bound.

## Reproduce

### Requirements

- Python 3.9+ (stdlib only, no pip installs)
- git
- Keys in `.env` (copy `.env.example`):
  - `PRIMALABS_BASE_URL`, `PRIMALABS_API_KEY` — open-model runs on PrimaLabs
  - `OPENROUTER_API_KEY` — closed-model and neutral-serving runs (full slate ≈ $60 with prompt caching; Anthropic `cache_control` is applied automatically)

### Pinned inputs

Reproducibility depends on three pinned artifacts, all in this repo or pinned by `scripts/reproduce.sh`:

| artifact | pin |
|---|---|
| Skill catalog | `genesis-skills` @ `70dce5ac` (2026-10-29); the script checks this out |
| Task set | `tasks/tasks.jsonl` (committed). **Do not regenerate** for comparison runs — `gen_tasks.py` samples at temperature 0.7 and produces a different set |
| Decoding | temperature 0, `max_tokens` 16384, 3 trials per condition |

Known nondeterminism: provider-side serving is not bit-reproducible at temperature 0 (we measured ±2–5pp across trials — hence 3 trials with mean±sd), and OpenRouter does not pin the underlying provider for open models. Model aliases resolve at call time; our runs used the model ids exactly as listed in `results/*.summary.json` on 2026-11-04/05.

### Run

```bash
git clone git@github.com:PrimaLabs-AI/genesis-skilleval.git && cd genesis-skilleval
cp .env.example .env   # fill in keys

SMOKE=1 ./scripts/reproduce.sh   # free-ish 8-task sanity check (~1 min)
./scripts/reproduce.sh           # full matrix (~2-3 h wall, ≈$60 OpenRouter + PrimaLabs usage)
```

All runs are resumable: per-trial results land in `results/<model>.<condition>.t<N>.jsonl` and `--resume` skips completed files, so interruptions never re-bill finished work.

Single model / condition:

```bash
python3 skilleval/run_eval.py --model nvidia/nemotron-3.5-super-vl --condition preload --trials 3 --resume
python3 skilleval/analyze.py > results/analysis.md
```

Model id routing: `primalabs-ai/*` → PrimaLabs endpoint; anything else → OpenRouter; `cli/claude/<model>` and `cli/codex/<model>` → local subscription CLIs (optional; harness-level numbers, reported separately in `report.md`).

### Verify against our numbers

`results/` contains every raw per-trial file from the published runs (including model replies, truncated to 500 chars). `python3 skilleval/analyze.py` regenerates all tables in `report.md` from them. A fresh run should match the committed means within the per-trial sd shown in `results/analysis.md`.

## Repo map

| path | contents |
|---|---|
| `skilleval/catalog.py` | SKILL.md discovery/parsing, disclosure + preload prompt blocks |
| `skilleval/client.py` | multi-provider chat client (PrimaLabs, OpenRouter, subscription CLIs), retries, Anthropic cache_control |
| `skilleval/gen_tasks.py` | task-set generator (DeepSeek as generator; only for building *new* task sets) |
| `skilleval/run_eval.py` | activation eval, 3 conditions, resumable trials |
| `skilleval/exec_eval.py` | execution pilot with LLM judge |
| `skilleval/analyze.py` | aggregate tables, per-domain recall, confusion pairs |
| `tasks/tasks.jsonl` | the 120 labeled tasks used in all published runs |
| `results/` | raw per-trial results + aggregate `analysis.md` |
| `scripts/reproduce.sh` | one-command reproduction (pins catalog, runs matrix, aggregates) |

## Caveats

Synthetic task set (DeepSeek-generated; human audit pending), single-label ground truth (deflates exact-match for legitimately multi-skill tasks), execution eval is chat-only, OpenRouter provider not pinned for open-model replication runs. Full list and discussion in `report.md`.

## License

Apache-2.0 (see `LICENSE`).
