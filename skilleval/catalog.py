"""Discover and parse Genesis Agent Skills (SKILL.md + YAML frontmatter)."""
from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path
from typing import List

SKILLS_ROOT = Path(__file__).resolve().parent.parent / "genesis-skills" / "skills"

_FRONTMATTER = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.DOTALL)


@dataclass
class Skill:
    name: str
    description: str
    body: str  # markdown after frontmatter
    path: Path
    domain: str


def _parse_frontmatter(text: str) -> dict:
    """Minimal YAML frontmatter parser: top-level `key: value` scalars only.

    Genesis skills use flat scalar frontmatter; nested values (metadata:) are
    ignored, which is fine since we only need name/description.
    """
    m = _FRONTMATTER.match(text)
    if not m:
        return {}
    out = {}
    key = None
    for line in m.group(1).splitlines():
        if line.startswith((" ", "\t")):
            # continuation of a folded/multiline value
            if key:
                out[key] += " " + line.strip()
            continue
        if ":" not in line:
            continue
        key, _, value = line.partition(":")
        key = key.strip()
        out[key] = value.strip().strip("\"'").lstrip(">|").strip()
    return out


def load_catalog(root: Path = SKILLS_ROOT) -> List[Skill]:
    skills = []
    for skill_md in sorted(root.rglob("SKILL.md")):
        text = skill_md.read_text(encoding="utf-8")
        fm = _parse_frontmatter(text)
        if not fm.get("name") or not fm.get("description"):
            continue
        body = _FRONTMATTER.sub("", text, count=1)
        domain = skill_md.relative_to(root).parts[0]
        skills.append(
            Skill(
                name=fm["name"],
                description=fm["description"],
                body=body,
                path=skill_md,
                domain=domain,
            )
        )
    return skills


def metadata_block(skills: List[Skill]) -> str:
    """Anthropic-style <available_skills> block: metadata only (condition A)."""
    lines = ["<available_skills>"]
    for s in skills:
        lines += [
            "<skill>",
            f"<name>{s.name}</name>",
            f"<description>{s.description}</description>",
            "</skill>",
        ]
    lines.append("</available_skills>")
    return "\n".join(lines)


def preload_block(skills: List[Skill]) -> str:
    """Full SKILL.md bodies inline (condition B)."""
    lines = ["<available_skills>"]
    for s in skills:
        lines += [
            "<skill>",
            f"<name>{s.name}</name>",
            f"<description>{s.description}</description>",
            "<instructions>",
            s.body.strip(),
            "</instructions>",
            "</skill>",
        ]
    lines.append("</available_skills>")
    return "\n".join(lines)


if __name__ == "__main__":
    cat = load_catalog()
    meta, pre = metadata_block(cat), preload_block(cat)
    print(f"{len(cat)} skills")
    print(f"metadata block: ~{len(meta) // 4} tokens")
    print(f"preload block:  ~{len(pre) // 4} tokens")
    for s in cat:
        print(f"  {s.domain:22s} {s.name}")
