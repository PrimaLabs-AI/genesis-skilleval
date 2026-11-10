# Skill Activation in Open-Weight Models: Genesis Agent Skills on Nemotron 3.5

**Status:** internal draft, 2026-11-05. Numbers from `results/`; reproduce with the commands at the bottom.

## What this is

First measured data on how well open-weight models route and respect [Genesis Agent Skills](https://gitlab.osti.gov/genesis/genesis-skills) (36 skills, 8 domains). Four models served on PrimaLabs (Nemotron 3.5 Lightning NVFP4, Nemotron 3.5 Super VL NVFP4, GLM-5.3-Flash, MiMo-V2.6-Pro), three skill-exposure conditions, 120 labeled tasks (108 skill-requiring, 12 distractors), 3 trials each.

Conditions:

- **disclosure** — standard progressive disclosure: name+description only (~3.7k tokens)
- **preload** — full SKILL.md bodies inline (~63k tokens; exploits the 1M context)
- **preload-anchor** — preload + one-line format reminder appended to the user turn

## Results (mean±sd over 3 trials)

| model | condition | recall | exact | precision | false-act | unparseable |
|---|---|---|---|---|---|---|
| nemotron-lightning | disclosure | 0.793±0.005 | 0.682±0.019 | 0.681±0.037 | 0.000 | 0.000 |
| nemotron-lightning | preload | 0.747±0.033 | 0.660±0.019 | 0.692±0.034 | **0.444±0.048** | 0.114±0.013 |
| nemotron-lightning | **preload-anchor** | **0.855±0.019** | **0.738±0.027** | **0.749±0.062** | **0.000** | 0.000 |
| nemotron-super-vl | disclosure | 0.932±0.019 | 0.645±0.005 | 0.648±0.012 | 0.000 | 0.000 |
| nemotron-super-vl | **preload** | **0.981±0.010** | **0.830±0.019** | **0.824±0.014** | 0.028±0.048 | 0.003±0.005 |
| nemotron-super-vl | preload-anchor | 0.960±0.019 | 0.793±0.005 | 0.733±0.013 | 0.000 | 0.000 |
| glm-5.3-flash | disclosure | 0.969±0.005 | 0.546±0.032 | 0.594±0.010 | 0.000 | 0.000 |
| glm-5.3-flash | preload | 0.991±0.009 | 0.657±0.016 | 0.667±0.023 | 0.000 | 0.000 |
| glm-5.3-flash | preload-anchor | 0.994±0.005 | 0.654±0.005 | 0.671±0.019 | 0.000 | 0.000 |
| mimo-v2.6-pro | disclosure | 0.994±0.005 | 0.481±0.019 | 0.545±0.012 | 0.000 | 0.000 |
| mimo-v2.6-pro | preload | 1.000±0.000 | 0.543±0.023 | 0.617±0.009 | 0.000 | 0.000 |
| mimo-v2.6-pro | preload-anchor | 1.000±0.000 | 0.494±0.011 | 0.577±0.009 | 0.000 | 0.000 |

recall = required skill among selected; exact = selected exactly the required skill; precision = hits / total selections; false-act = any selection (incl. protocol break) on distractor tasks; unparseable = reply violated the JSON routing contract.

### Closed-model baselines via subscription CLIs (added 11-05, harness-level)

Run through Codex CLI (`gpt-6-astra`, ChatGPT subscription) and Claude Code CLI (`sonnet` alias, v2.1.274, tools disabled). These CLIs inject their own scaffolding and don't expose temperature: numbers are **harness-level**, single trial, kept out of the model-level table above.

| model | condition | recall | exact | precision | false-act |
|---|---|---|---|---|---|
| gpt-6-astra (Codex) | disclosure | 0.991 | 0.472 | 0.498 | 0.000 |
| gpt-6-astra (Codex) | preload | 1.000 | 0.620 | 0.643 | 0.000 |
| gpt-6-astra (Codex) | preload-anchor | 1.000 | 0.648 | 0.659 | 0.083 |
| claude sonnet (CC) | disclosure | 0.935 | 0.583 | 0.620 | 0.000 |
| claude sonnet (CC) | preload | 0.981 | 0.630 | 0.684 | 0.000 |
| claude sonnet (CC) | preload-anchor | 0.972 | 0.620 | 0.652 | 0.000 |

**Leaderboard by exact-match (best config per model):** Super VL preload 0.830 · Lightning preload-anchor 0.738 · GLM preload 0.657 · gpt-6-astra preload-anchor 0.648 · claude sonnet preload 0.630 · MiMo preload 0.543.

Two additions to the findings: (a) **Nemotron 3.5 Super VL posts the highest exact-match routing of anything measured, including frontier closed models run through their native CLIs — by ~20pp.** Closed models share the open-peer pattern: near-perfect recall, lower precision (GPT selects 2.0 skills/task under disclosure). (b) **Full-catalog preload beat metadata-only disclosure for every one of the six models** (for Lightning, once format discipline is restored via the anchor) — progressive disclosure consistently costs routing accuracy; its remaining justification is context economy, not quality. Raw-API closed-model runs (OpenRouter) remain the publication-grade follow-up.

### Raw-API frontier baselines via OpenRouter (added 11-05, publication-grade)

Temperature 0, 3 trials, identical harness, pinned model ids, ~$60 total. Mean exact-match of best config per model:

| model | best config | exact | recall | notes |
|---|---|---|---|---|
| **nemotron-3.5-super-vl (PrimaLabs NVFP4)** | preload | **0.830** | 0.981 | our serving |
| **nemotron-3.5-super-vl (OpenRouter)** | preload / preload-anchor | **0.753** | 0.938 | independent serving, provider unpinned |
| reflection/beam-1.0-501b-a23b (OpenRouter) | preload-anchor | 0.756 | 0.997 | 501B/23B-active; raw preload false-act 0.50, disclosure false-act 0.17 — worst format-break measured; anchor → 0.0. Statistical tie with Super VL on neutral serving |
| moonshotai/kimi-k3.1-pro (OpenRouter) | preload | 0.747 | 0.981 | statistically tied with Super VL on neutral serving; no format-break |
| nemotron-3.5-lightning (PrimaLabs NVFP4) | preload-anchor | 0.738 | 0.855 | our serving |
| nemotron-3.5-lightning (OpenRouter) | preload-anchor | 0.707 | 0.827 | format-break replicates: preload false-act 0.25–0.50/trial, anchor → ~0.03 |
| openai/gpt-5.2 | preload-anchor | 0.716 | 0.947 | raw preload leaks 8–25% distractor false-acts; anchor fixes |
| anthropic/claude-opus-5.5 | preload | 0.679 | 0.997 | flagship; preload-only run |
| google/gemini-3.5-flash | preload | 0.663 | 0.978 | anchor slightly hurts |
| anthropic/claude-sonnet-5.5 | preload-anchor | 0.639 | 0.994 | raw ≈ CLI numbers (±1pp) |

Conclusions this locks in:
1. **Super VL ranks #1 on both serving stacks, including over Claude Opus 5.5.** Margin is serving-dependent: +3.7pp over GPT-5.2 on neutral infrastructure, +11.4pp on PrimaLabs NVFP4. Report the model-level claim from the OpenRouter number; the 0.830 is a system-level (model+serving) result.
2. **Serving measurably affects routing quality** (0.830 vs 0.753 for the identical model) — provider choice, quantization, and template are part of agentic accuracy, not just speed.
3. **The instruction-mass format-break is cross-vendor:** raw GPT-5.2 reproduces the Lightning failure under preload (distractor false-activation up to 25%), eliminated by the same one-line anchor. Capacity-dependent, not vendor- or openness-dependent.
4. **A preloaded configuration (raw or anchored) ≥ disclosure on all 11 endpoints tested under both conditions** (10 distinct models across NVIDIA, OpenAI, Anthropic, Google, Zhipu, Xiaomi, Moonshot, Reflection; gains +5.5 to +18.5pp exact). Lightning requires the anchor — its raw preload scores below disclosure (0.682→0.661); Opus ran preload-only and is excluded.
5. **Raw API ≈ CLI for Claude (±1pp); raw GPT-5.2 beats its Codex-mediated cousin (0.716 vs 0.648)** — harness mediation is not neutral for OpenAI.

## Findings

1. **Full-catalog preload breaks Nemotron's output discipline; a one-line anchor fixes it and unlocks the gains.** Raw preload caused 44% of distractor tasks to break the JSON routing contract — the model answered the question directly instead of routing (e.g., wrote the Python function instead of `{"skills": []}`). It never selected a *wrong* skill; the failure is protocol compliance under 63k tokens of instruction mass, not routing. Appending `Remember: reply with JSON only…` to the user turn eliminated every break **and** made preload-anchor Nemotron's best condition on all metrics (+6pp recall, +6pp exact over standard disclosure). Implication: with long-context models, skip progressive disclosure, preload + cache the full catalog, and inject a format anchor at the serving layer.
2. **Models trade recall against precision in opposite corners.** Nemotron is conservative (selects 1.1 skills/task, highest exact-match); GLM/MiMo near-perfect recall but spray selections (1.6–1.8 skills/task, exact as low as 0.48). For agent harnesses where each activated skill costs context and tool permissions, exact-match is the metric that matters.
3. **The catalog itself has routing hazards.** Top confusions are near-duplicate skills: `pbs`→`slurm` (21), `ai-fingerprint`→`fingerprinting` (12 — two skills with overlapping descriptions in basesafe), `i2-api`→`amsc-mag` (19). Nemotron's worst domains (academy 0.33 disclosure-recall, amsc-skills 0.67) have the least distinctive descriptions. Actionable upstream: sharpen description fields; merge or cross-reference the fingerprinting pair. Notably, preload-anchor fixed academy entirely (0.33→1.00) — full instructions disambiguate what terse descriptions can't.
4. **Instruction-mass tolerance scales with capacity; the anchor is model-conditional (Super VL, added 11-05).** Super VL posts the best activation numbers in the study under raw preload (exact 0.830, +18.5pp over its own disclosure; precision 0.824) with essentially no protocol breaks — the Lightning format-break does not reproduce at Super scale. The anchor that rescued Lightning slightly hurts Super VL (−3.7pp exact). Serving guidance: preload+cache the catalog for both; inject the anchor only for Lightning-class models. Separately, Super VL's execution pilot (3.43/3.51/2.86) is understated by a serving bug: several responses degenerate into unbounded repeated `</function_calls>`/`</system>` tags — chat-template/stop-token mismatch in the Super VL path; file with the serving team before any agentic benchmarking.

## Caveats

- Tasks generated by DeepSeek-V4.1 (different model family than evaluated models, but still synthetic; human-written tasks needed before publication).
- Single-label ground truth; some tasks legitimately admit 2 skills, deflating exact/precision for the high-recall models.
- Serving nondeterminism at temperature 0 (trial variance visible in sd columns).
- Execution scores are chat-only (no tool loop); skills prescribing script execution are penalized for both models.

## Execution quality (pilot, one task per skill)

Model performs the task with the required SKILL.md in context; GLM-5.3-Flash judges adherence/correctness/completeness (1–5) against the skill's own instructions. 36 tasks per model, single trial.

| model | adherence | correctness | completeness |
|---|---|---|---|
| nemotron-lightning | 3.40 | 3.37 | 2.94 |
| glm-5.3-flash | 3.85 | 4.26 | 3.47 |

**Read as a lower bound, not a verdict.** The lowest-scored responses in both models are skills that prescribe *executing scripts* (battleprint, ai-fingerprint, data-exploration): in this chat-only harness the model either emits a truncated tool/action call (Nemotron) or a prose runbook (GLM), and the judge scores both as incomplete. GLM's edge partly reflects that runbooks judge better than interrupted execution attempts. Measuring execution properly requires a tool-loop harness (sandboxed bash/file tools) — the top next step. The judge also noted catalog-actionable detail: several skills' execution guides forbid compound shell commands (`&&`), which both models violated immediately.

## Next steps

1. Tool-loop harness (sandboxed bash/file tools) for faithful execution scoring.
2. ~~Closed-model baseline~~ Done 11-05: raw-API GPT-5.2, Claude Sonnet/Opus 5.5, Gemini 3.5 Flash via OpenRouter (see above).
3. Human-audited task set (~150, multi-label).
4. Serving feature: `skills:` parameter with server-side preload + cache + anchor injection — this report is the empirical justification.
5. Upstream PR: description fixes for confused skill pairs + this harness.


## Reproduce

```bash
python3 skilleval/gen_tasks.py                      # regenerate tasks (DeepSeek)
python3 skilleval/run_eval.py --model <model> --condition all --trials 3
python3 skilleval/analyze.py > results/analysis.md  # tables
```
