"""Generate labeled eval tasks from skill descriptions.

Generator model (DeepSeek) differs from the evaluated model (Nemotron) to
avoid self-generation bias. Each skill yields N user-style tasks labeled
required=<skill>; distractor tasks require no skill at all.
"""
from __future__ import annotations

import json
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from catalog import load_catalog
from client import DEEPSEEK, chat, extract_json

OUT = Path(__file__).resolve().parent.parent / "tasks" / "tasks.jsonl"
TASKS_PER_SKILL = 3
N_DISTRACTORS = 12

GEN_PROMPT = """You are building an evaluation set for AI scientific agents.

Below is an agent skill (name, description, and instructions excerpt):

name: {name}
description: {description}
instructions excerpt:
{body}

Write {n} realistic user requests that a scientist might type to an AI agent, where correctly handling the request requires THIS skill. Rules:
- Vary phrasing, specificity, and user persona; do NOT mention the skill name or quote its description.
- Each request must be self-contained, 1-3 sentences.
- At least one request should be indirect (the user does not realize a specialized workflow exists).

Reply with JSON only: {{"tasks": ["...", "..."]}}"""

DISTRACTOR_PROMPT = """You are building an evaluation set for AI scientific agents. The agent has specialized skills for: literature search, HPC job submission (Slurm/PBS, Frontier/Aurora/Perlmutter), plasma simulation, scientific data cards/metadata, AI safety red-teaming, uncertainty quantification, multi-agent system design, and DOE data-movement APIs.

Write {n} realistic user requests that require NONE of those skills: generic coding help, basic math, writing assistance, or general science questions answerable directly. 1-3 sentences each.

Reply with JSON only: {{"tasks": ["...", "..."]}}"""


def gen_for_skill(skill):
    prompt = GEN_PROMPT.format(
        name=skill.name,
        description=skill.description,
        body=skill.body[:3000],
        n=TASKS_PER_SKILL,
    )
    for attempt in range(3):
        reply = chat(
            [{"role": "user", "content": prompt}],
            model=DEEPSEEK,
            temperature=0.7,
            max_tokens=8192,
        )
        try:
            tasks = extract_json(reply)["tasks"][:TASKS_PER_SKILL]
            break
        except (ValueError, KeyError):
            if attempt == 2:
                raise
    return [
        {"id": f"{skill.name}-{i}", "task": t, "required": skill.name, "domain": skill.domain}
        for i, t in enumerate(tasks)
    ]


def main():
    catalog = load_catalog()
    OUT.parent.mkdir(exist_ok=True)
    rows = []
    with ThreadPoolExecutor(max_workers=8) as pool:
        for result in pool.map(gen_for_skill, catalog):
            rows.extend(result)
            print(f"  {result[0]['required']}: {len(result)} tasks", file=sys.stderr)
    reply = chat(
        [{"role": "user", "content": DISTRACTOR_PROMPT.format(n=N_DISTRACTORS)}],
        model=DEEPSEEK,
        temperature=0.7,
    )
    for i, t in enumerate(extract_json(reply)["tasks"][:N_DISTRACTORS]):
        rows.append({"id": f"none-{i}", "task": t, "required": None, "domain": "none"})
    with OUT.open("w") as f:
        for r in rows:
            f.write(json.dumps(r) + "\n")
    print(f"wrote {len(rows)} tasks -> {OUT}")


if __name__ == "__main__":
    main()
