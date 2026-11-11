# Why Skill Routing Decides Whether Science Agents Can Be Trusted
### Genesis-SkillEval, the first benchmark of DOE's Genesis Agent Skills — and what it tells us about building AI agents for science
*PrimaLabs · November 2026*

## The problem nobody benchmarks

The Genesis Mission is standing up AI agents that plan experiments, steer simulations, move data between national laboratories, and submit jobs to the nation's largest supercomputers. In October, DOE released [Genesis Agent Skills](https://gitlab.osti.gov/genesis/genesis-skills) — the first shared catalog of validated agent workflows, built by the national laboratory system: how to submit to Frontier and Perlmutter, how to move data through the American Science Cloud, how to run uncertainty quantification, how to red-team an agent before it touches controlled data.

A catalog is only as good as an agent's ability to pick the right entry. Every agent action starts with a routing decision: *this request needs the Slurm skill, not the PBS skill; the UQ skill, not a guess.* Pick wrong and the agent improvises exactly where DOE built the catalog to stop improvisation. Pick three skills instead of one and the agent acquires tool permissions and context it shouldn't have — in a setting where actions are audited and the data may be export-controlled. For science agents, **skill routing is a safety and reproducibility property, not a convenience.**

No one had measured it. We built the first routing benchmark for the Genesis catalog — all 36 skills, 120 labeled scientist-style requests, ten models from eight vendors (twelve model×serving endpoints), raw APIs, repeated trials — and measured who activates *exactly* the right skill.

## What we found

**1. The best router on DOE's catalog is an open, U.S.-developed model.**
NVIDIA's open-weight Nemotron 3.5 Super VL scored highest on exact-match routing of all ten models — above GPT-5.2, Claude Opus 5.5, and Gemini 3.5 Flash, and in a statistical tie with the strongest other open models (Reflection Beam 1.0 at 0.756, Kimi K3.1 Pro at 0.747) — on neutral third-party serving (0.753 vs 0.716 for the best closed model) and by a wider margin on optimized serving (0.830). Closed frontier models found the right skill but consistently over-activated: ~1.6 skills per request under standard disclosure, 1.3–1.5 even in their best configurations, versus 1.2 for Super VL. This matters because the Genesis Mission's most sensitive deployments — air-gapped enclaves, export-controlled data — favor models a lab can run fully on-premises, pin, inspect, and audit, a property open weights provide by default. The result says that path carries **no capability penalty** for skill-governed science agents. Sovereignty and performance are not in tension.

| model | serving | exact-match routing | skills activated per task |
|---|---|---|---|
| **Nemotron 3.5 Super VL** (open) | PrimaLabs (NVFP4) | **0.830** | 1.2 |
| Reflection Beam 1.0 (open) | OpenRouter | 0.756 | 1.3 |
| **Nemotron 3.5 Super VL** (open) | OpenRouter (neutral) | **0.753** | 1.2 |
| Kimi K3.1 Pro (open) | OpenRouter | 0.747 | 1.3 |
| Nemotron 3.5 Lightning (open) | PrimaLabs | 0.738 | 1.2 |
| GPT-5.2 | OpenRouter | 0.716 | 1.3 |
| Nemotron 3.5 Lightning (open) | OpenRouter (neutral) | 0.707 | 1.3 |
| Claude Opus 5.5 | OpenRouter | 0.679 | 1.4 |
| Gemini 3.5 Flash | OpenRouter | 0.663 | 1.4 |
| GLM-5.3-Flash (open) | PrimaLabs | 0.657 | 1.5 |
| Claude Sonnet 5.5 | OpenRouter | 0.639 | 1.5 |
| MiMo-V2.6-Pro (open) | PrimaLabs | 0.543 | 1.6 |

*Best configuration per model; mean of 3 trials at temperature 0; exact-match = activated precisely the required skill and nothing else. Full per-condition tables in the benchmark report.*

**2. How skills are loaded changes how well they work — for every model.**
The skill standard loads only a skill's name and one-line description at routing time, to save context. We found that putting the *full instructions* of all 36 skills in context (~63k tokens, cached) beat disclosure on **every endpoint tested under both conditions, by 5.5–18.5 points** — for one model (Nemotron Lightning) only with a one-line format anchor, and with Claude Opus untested under disclosure. Long-context models and cheap cached serving have quietly removed the constraint the convention was designed around. For Genesis, this is actionable today: a one-line change to how skills are served makes every agent in the ecosystem more accurate, at near-zero marginal cost.

**3. Agents fail in a way benchmarks don't catch — and infrastructure can fix.**
Under heavy in-context instruction load, mid-capacity models from multiple vendors (NVIDIA and OpenAI alike) stopped following the agent's output protocol on out-of-scope requests — answering directly instead of routing, in up to 44% of cases. In production, that silently breaks the pipeline that enforces governance. A single serving-side guard line eliminated the failure entirely. The lesson for Genesis: **agent reliability is partly a serving-infrastructure property.** The same model scored 0.830 and 0.753 depending on who served it. Provider choice, quantization, and configuration belong in the mission's assurance story, alongside model choice.

**4. The benchmark hardens the catalog itself.**
Systematic confusions between near-duplicate skills (PBS vs Slurm; two overlapping fingerprinting skills) point to specific, fixable catalog improvements — and show that a routing benchmark can serve as a regression test for every future skill contribution. We are contributing the harness and fixes upstream.

## Why this is critical for the Genesis Mission

The Genesis Mission's bet is that agents can accelerate science *without* sacrificing the things science runs on: reproducibility, provenance, and control of sensitive data. These results bear directly on that bet. They show the skills architecture works — and works best — with open models that labs can deploy on their own terms, inspect, pin, and audit. They show that measured, public evaluation finds real failure modes (and real fixes) before deployment does. And they show the catalog, two weeks after release, already functioning as what it was designed to be: shared infrastructure that gets better because everyone can test against it.

Agents will soon propose formulations for nuclear-waste vitrification, steer plasma simulations, and triage experimental data across the laboratory system. Whether to trust them starts with a measurable question: *do they reliably do the validated thing rather than the plausible thing?* That is now a number, for ten models, on DOE's own catalog — and the answer favors the open path the Genesis Mission is built on.

---
*Benchmark harness, raw data, and full methodology (including caveats: synthetic task set, single-label ground truth) are available for review and reproduction. Contact: Prasanna Balaprakash, PrimaLabs.*
