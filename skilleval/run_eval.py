"""Skill-activation eval: Nemotron must pick the right skill(s) for each task.

Conditions:
  disclosure — metadata-only <available_skills> (standard progressive disclosure)
  preload    — full SKILL.md bodies inline (~63k tokens; exploits 1M context)

Metrics per condition: exact-match accuracy, precision/recall over selected
skills, false-activation rate on distractor tasks.
"""
from __future__ import annotations

import argparse
import json
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from catalog import load_catalog, metadata_block, preload_block
from client import LIGHTNING, chat, extract_json

ROOT = Path(__file__).resolve().parent.parent
TASKS = ROOT / "tasks" / "tasks.jsonl"
RESULTS = ROOT / "results"

SYSTEM = """You are a scientific AI agent. You have access to the following agent skills. Before answering any request, decide which skills (if any) you would activate to handle it correctly.

{skills_block}

For the user's request, reply with JSON only, no other text:
{{"skills": ["skill-name", ...]}}
Use the exact skill names. Use an empty list if no skill is needed."""

ANCHOR = '\n\nRemember: reply with JSON only, {"skills": [...]} — do not answer the request itself.'


def evaluate(task_row, skills_block, model, anchor=False):
    user = task_row["task"] + (ANCHOR if anchor else "")
    try:
        reply = chat(
            [
                {"role": "system", "content": SYSTEM.format(skills_block=skills_block)},
                {"role": "user", "content": user},
            ],
            model=model,
            max_tokens=16384,
        )
    except RuntimeError as e:
        return {**task_row, "selected": ["<error>"], "raw": str(e)[:300]}
    try:
        selected = extract_json(reply).get("skills", [])
        if not isinstance(selected, list):
            selected = []
        selected = [str(s) for s in selected]
    except ValueError:
        selected = ["<unparseable>"]
    return {**task_row, "selected": selected, "raw": reply[-500:]}


def metrics(rows):
    skill_rows = [r for r in rows if r["required"]]
    distractors = [r for r in rows if not r["required"]]
    hit = sum(r["required"] in r["selected"] for r in skill_rows)
    exact = sum(r["selected"] == [r["required"]] for r in skill_rows)
    n_selected = sum(len(r["selected"]) for r in skill_rows)
    false_act = sum(bool(r["selected"]) for r in distractors)
    return {
        "n_skill_tasks": len(skill_rows),
        "n_distractors": len(distractors),
        "recall": round(hit / len(skill_rows), 3) if skill_rows else None,
        "exact_match": round(exact / len(skill_rows), 3) if skill_rows else None,
        "precision": round(hit / n_selected, 3) if n_selected else None,
        "avg_selected": round(n_selected / len(skill_rows), 2) if skill_rows else None,
        "false_activation_rate": round(false_act / len(distractors), 3) if distractors else None,
    }


CONDITIONS = {
    "disclosure": (metadata_block, False),
    "preload": (preload_block, False),
    "preload-anchor": (preload_block, True),
}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--condition", choices=[*CONDITIONS, "all"], default="all")
    ap.add_argument("--model", default=LIGHTNING)
    ap.add_argument("--limit", type=int, default=0, help="limit tasks (pilot)")
    ap.add_argument("--workers", type=int, default=8)
    ap.add_argument("--trials", type=int, default=1)
    ap.add_argument("--resume", action="store_true", help="skip existing result files")
    args = ap.parse_args()

    catalog = load_catalog()
    tasks = [json.loads(l) for l in TASKS.read_text().splitlines()]
    if args.limit:
        tasks = tasks[: args.limit]
    RESULTS.mkdir(exist_ok=True)

    slug = args.model.rsplit("/", 1)[-1].lower()
    conditions = list(CONDITIONS) if args.condition == "all" else [args.condition]
    summary = {}
    for cond in conditions:
        block_fn, anchor = CONDITIONS[cond]
        block = block_fn(catalog)
        summary[cond] = []
        for trial in range(args.trials):
            out = RESULTS / f"{slug}.{cond}.t{trial}.jsonl"
            if args.resume and out.exists():
                rows = [json.loads(l) for l in out.read_text().splitlines()]
                summary[cond].append(metrics(rows))
                print(f"[{slug} {cond} t{trial}] resumed from disk", file=sys.stderr)
                continue
            with ThreadPoolExecutor(max_workers=args.workers) as pool:
                rows = list(
                    pool.map(lambda t: evaluate(t, block, args.model, anchor=anchor), tasks)
                )
            with out.open("w") as f:
                for r in rows:
                    f.write(json.dumps(r) + "\n")
            summary[cond].append(metrics(rows))
            print(f"[{slug} {cond} t{trial}] {summary[cond][-1]}", file=sys.stderr)

    (RESULTS / f"{slug}.summary.json").write_text(json.dumps(summary, indent=2))
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
