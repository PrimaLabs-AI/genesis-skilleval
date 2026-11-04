"""Aggregate eval results: mean±sd across trials, per-domain errors, confusions."""
from __future__ import annotations

import json
import statistics
from collections import Counter, defaultdict
from pathlib import Path

RESULTS = Path(__file__).resolve().parent.parent / "results"
METRICS = ["recall", "exact_match", "precision", "false_activation_rate"]


def load_runs():
    """-> {model: {condition: [rows_per_trial]}}"""
    runs = defaultdict(lambda: defaultdict(list))
    for f in sorted(RESULTS.glob("*.t*.jsonl")):
        model, cond, _trial = f.stem.rsplit(".", 2)
        runs[model][cond].append([json.loads(l) for l in f.read_text().splitlines()])
    return runs


def summary_table(runs):
    lines = ["| model | condition | recall | exact | precision | false-act | unparse |", "|---|---|---|---|---|---|---|"]
    for model, conds in runs.items():
        for cond, trials in conds.items():
            agg = defaultdict(list)
            for rows in trials:
                skill = [r for r in rows if r["required"]]
                dis = [r for r in rows if not r["required"]]
                sel = sum(len(r["selected"]) for r in skill)
                agg["recall"].append(sum(r["required"] in r["selected"] for r in skill) / len(skill))
                agg["exact"].append(sum(r["selected"] == [r["required"]] for r in skill) / len(skill))
                agg["precision"].append(
                    sum(r["required"] in r["selected"] for r in skill) / sel if sel else 0.0
                )
                agg["false"].append(sum(bool(r["selected"]) for r in dis) / len(dis))
                agg["unparse"].append(
                    sum("<unparseable>" in r["selected"] for r in rows) / len(rows)
                )

            def fmt(k):
                vals = agg[k]
                mean = statistics.mean(vals)
                sd = statistics.stdev(vals) if len(vals) > 1 else 0.0
                return f"{mean:.3f}±{sd:.3f}"

            lines.append(
                f"| {model} | {cond} | {fmt('recall')} | {fmt('exact')} | {fmt('precision')} | {fmt('false')} | {fmt('unparse')} |"
            )
    return "\n".join(lines)


def domain_table(runs):
    lines = ["| model | condition | domain | recall |", "|---|---|---|---|"]
    for model, conds in runs.items():
        for cond, trials in conds.items():
            by_domain = defaultdict(lambda: [0, 0])
            for rows in trials:
                for r in rows:
                    if not r["required"]:
                        continue
                    by_domain[r["domain"]][1] += 1
                    by_domain[r["domain"]][0] += r["required"] in r["selected"]
            for dom, (hit, n) in sorted(by_domain.items(), key=lambda kv: kv[1][0] / kv[1][1]):
                lines.append(f"| {model} | {cond} | {dom} | {hit}/{n} ({hit/n:.2f}) |")
    return "\n".join(lines)


def confusions(runs, top=15):
    pairs = Counter()
    for model, conds in runs.items():
        for cond, trials in conds.items():
            for rows in trials:
                for r in rows:
                    req = r["required"]
                    if not req or req in r["selected"]:
                        continue
                    for s in r["selected"]:
                        if s != "<unparseable>":
                            pairs[(req, s)] += 1
                    if not r["selected"]:
                        pairs[(req, "<nothing>")] += 1
    lines = ["| required | selected instead | count |", "|---|---|---|"]
    for (req, sel), n in pairs.most_common(top):
        lines.append(f"| {req} | {sel} | {n} |")
    return "\n".join(lines)


if __name__ == "__main__":
    runs = load_runs()
    print("## Summary (mean±sd over trials)\n")
    print(summary_table(runs))
    print("\n## Per-domain recall (worst first)\n")
    print(domain_table(runs))
    print("\n## Top confusions (all models/conditions pooled)\n")
    print(confusions(runs))
