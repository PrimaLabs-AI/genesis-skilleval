"""Execution-quality eval: model performs the task WITH the required SKILL.md
in context; a judge model scores adherence to the skill's instructions.

Judge = GLM-5.3-Flash (different family from evaluated models where possible);
judge sees the skill instructions + task + response, scores 1-5 on a fixed
rubric. One task per skill (the "-0" task) to keep cost bounded.
"""
from __future__ import annotations

import argparse
import json
import statistics
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from catalog import load_catalog
from client import LIGHTNING, chat, extract_json

ROOT = Path(__file__).resolve().parent.parent
TASKS = ROOT / "tasks" / "tasks.jsonl"
RESULTS = ROOT / "results"
JUDGE = "primalabs-ai/GLM-5.3-Flash"

EXEC_SYSTEM = """You are a scientific AI agent. The following agent skill is activated for this request. Follow its instructions. If the task requires running commands or accessing systems you cannot reach, produce the exact artifacts (scripts, commands, configurations, plans) the skill prescribes, stating any assumptions.

<skill name="{name}">
{body}
</skill>"""

JUDGE_PROMPT = """You are auditing whether an AI agent followed a prescribed skill when answering a user request.

<skill_instructions>
{body}
</skill_instructions>

<user_request>
{task}
</user_request>

<agent_response>
{response}
</agent_response>

Score the response on each criterion, integers 1-5 (5 = fully satisfied):
- adherence: followed the skill's prescribed workflow/steps/tools rather than improvising
- correctness: technically plausible and consistent with the skill's domain specifics (APIs, flags, file formats, names)
- completeness: addressed the request end-to-end per the skill, stated assumptions where blocked

Reply with JSON only:
{{"adherence": n, "correctness": n, "completeness": n, "evidence": "one sentence citing the decisive detail"}}"""


def run_one(task_row, skill, model):
    response = chat(
        [
            {"role": "system", "content": EXEC_SYSTEM.format(name=skill.name, body=skill.body)},
            {"role": "user", "content": task_row["task"]},
        ],
        model=model,
        max_tokens=16384,
    )
    verdict_raw = chat(
        [
            {
                "role": "user",
                "content": JUDGE_PROMPT.format(
                    body=skill.body[:12000], task=task_row["task"], response=response[:12000]
                ),
            }
        ],
        model=JUDGE,
        max_tokens=8192,
    )
    try:
        v = extract_json(verdict_raw)
        scores = {k: int(v[k]) for k in ("adherence", "correctness", "completeness")}
        evidence = str(v.get("evidence", ""))
    except (ValueError, KeyError, TypeError):
        scores, evidence = {}, f"judge unparseable: {verdict_raw[:150]}"
    return {
        "id": task_row["id"],
        "skill": skill.name,
        "scores": scores,
        "evidence": evidence,
        "response_excerpt": response[:400],
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", default=LIGHTNING)
    ap.add_argument("--workers", type=int, default=4)
    args = ap.parse_args()

    skills = {s.name: s for s in load_catalog()}
    tasks = [
        json.loads(l)
        for l in TASKS.read_text().splitlines()
        if json.loads(l)["id"].endswith("-0") and json.loads(l)["required"]
    ]
    slug = args.model.rsplit("/", 1)[-1].lower()

    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        rows = list(pool.map(lambda t: run_one(t, skills[t["required"]], args.model), tasks))

    out = RESULTS / f"{slug}.exec.jsonl"
    with out.open("w") as f:
        for r in rows:
            f.write(json.dumps(r) + "\n")

    scored = [r for r in rows if r["scores"]]
    summary = {
        "model": args.model,
        "n": len(rows),
        "n_scored": len(scored),
        **{
            k: round(statistics.mean(r["scores"][k] for r in scored), 2)
            for k in ("adherence", "correctness", "completeness")
        },
    }
    print(json.dumps(summary, indent=2))
    worst = sorted(scored, key=lambda r: sum(r["scores"].values()))[:5]
    for r in worst:
        print(f"  LOW {r['skill']}: {r['scores']} — {r['evidence'][:140]}", file=sys.stderr)


if __name__ == "__main__":
    main()
