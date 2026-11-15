#!/usr/bin/env python3
"""Checks for the storyboard (storyboard/scenes.tsv) and the clue ledger (mystery/clues.tsv).

Storyboard:
  - date rewinds within the present-day story (interludes, id ending -X, are exempt)
  - scenes where nothing changes (empty what_changes)
  - dependencies that point forward or to unknown scenes
  - empty pov_lens
  - movement word totals against the contract (movements not yet storyboarded are listed)
  - POV absences: Tamsin over --main-gap words, other POVs over --gap words
  - where the 375th anniversary (first scene dated on or after 1022-04-09) falls

Clue ledger (fair play):
  - every clue of kind "plant" is planted in an earlier movement than the one where its meaning turns
  - a clue of kind "find" is not found after it turns
  - a clue planted at a scene id names a scene that exists (once its movement is storyboarded)
    and that scene lists the clue in its clues column, and vice versa
  - clues planted in a storyboarded movement but not yet given a scene are listed

Prints a report; exits 1 on any FAIL.
"""
import argparse
import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MOVEMENTS = ["I", "II", "III", "IV", "V", "VI"]
BUDGET = {"I": 14000, "II": 15000, "III": 16000, "IV": 17000, "V": 15000, "VI": 11000}
MAIN_POV = "TAM"
ANNIVERSARY = (1022, 4, 9)


def date_key(d):
    """'1021-12-14', '1022-04', '1022' -> sortable tuple."""
    parts = [int(p) for p in d.split("-") if p.isdigit()]
    while len(parts) < 3:
        parts.append(15 if len(parts) == 2 else 6)
    return tuple(parts[:3])


def movement_of(ref, scene_movement):
    """A clue's planted/turns field is a scene id ('I-05') or a movement ('III')."""
    if ref in scene_movement:
        return scene_movement[ref]
    m = re.match(r"^(I|II|III|IV|V|VI)(?:-|$)", ref)
    return m.group(1) if m else None


def read_tsv(path):
    with open(path, encoding="utf-8") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--gap", type=int, default=15000, help="longest absence for a secondary POV, in words")
    ap.add_argument("--main-gap", type=int, default=6000, help="longest absence for Tamsin, in words")
    args = ap.parse_args()

    rows = read_tsv(ROOT / "storyboard" / "scenes.tsv")
    clues = read_tsv(ROOT / "mystery" / "clues.tsv")
    errors, warnings = [], []

    pos = {r["id"]: i for i, r in enumerate(rows)}
    scene_movement = {r["id"]: r["movement"] for r in rows}
    is_interlude = lambda r: r["id"].endswith("-X")
    scenes = [r for r in rows if not is_interlude(r)]
    interludes = [r for r in rows if is_interlude(r)]

    # --- storyboard ---
    for prev, cur in zip(scenes, scenes[1:]):
        if date_key(cur["date"]) < date_key(prev["date"]):
            errors.append(f"rewind: {cur['id']} ({cur['date']}) after {prev['id']} ({prev['date']})")

    for r in rows:
        if r["movement"] not in MOVEMENTS:
            errors.append(f"movement: {r['id']} has unknown movement {r['movement']!r}")
        if not is_interlude(r):
            if not r["what_changes"].strip():
                errors.append(f"static: {r['id']} has no change")
            if not r["pov_lens"].strip():
                warnings.append(f"lens: {r['id']} has no pov_lens")
        for dep in filter(None, re.split(r"[ ,]+", r["depends_on"])):
            if dep not in pos:
                errors.append(f"dependency: {r['id']} depends on unknown {dep}")
            elif pos[dep] >= pos[r["id"]]:
                errors.append(f"dependency: {r['id']} depends on later scene {dep}")

    total = sum(int(r["words"]) for r in scenes)
    run, starts = 0, []
    for r in scenes:
        starts.append(run)
        run += int(r["words"])

    by_pov = {}
    for r, s in zip(scenes, starts):
        by_pov.setdefault(r["pov"], []).append((s, s + int(r["words"]), r["id"]))
    gaps = []
    for pov, spans in by_pov.items():
        limit = args.main_gap if pov == MAIN_POV else args.gap
        last_end, last_id = spans[0][1], spans[0][2]
        if spans[0][0] > limit:
            gaps.append((spans[0][0], pov, "start", spans[0][2]))
        for s, e, sid in spans[1:]:
            if s - last_end > limit:
                gaps.append((s - last_end, pov, last_id, sid))
            last_end, last_id = e, sid
        if total - last_end > limit:
            gaps.append((total - last_end, pov, last_id, "end"))

    # --- clues ---
    clue_ids = {c["id"] for c in clues}
    storyboarded = {r["movement"] for r in rows}
    listed = {}
    for r in rows:
        for cid in filter(None, re.split(r"[ ,]+", r.get("clues", ""))):
            listed.setdefault(cid, []).append(r["id"])
            if cid not in clue_ids:
                errors.append(f"clue: {r['id']} lists unknown clue {cid}")

    unassigned = []
    for c in clues:
        p, t = c["planted"].strip(), c["turns"].strip()
        pm, tm = movement_of(p, scene_movement), movement_of(t, scene_movement)
        if pm is None or tm is None:
            errors.append(f"clue: {c['id']} has an unreadable planted ({p!r}) or turns ({t!r})")
            continue
        pi, ti = MOVEMENTS.index(pm), MOVEMENTS.index(tm)
        if c["kind"] == "plant" and pi >= ti:
            errors.append(f"fair play: {c['id']} is a plant but is planted in {pm} and turns in {tm}")
        if c["kind"] == "find" and pi > ti:
            errors.append(f"fair play: {c['id']} turns in {tm} before it is found in {pm}")
        if c["kind"] not in ("plant", "find"):
            errors.append(f"clue: {c['id']} has kind {c['kind']!r} (plant or find)")
        if "-" in p:  # a scene id
            if p not in pos:
                if pm in storyboarded:
                    errors.append(f"clue: {c['id']} is planted at {p}, which is not in the storyboard")
            elif p not in listed.get(c["id"], []):
                errors.append(f"clue: {c['id']} is planted at {p}, but {p} does not list it")
        elif pm in storyboarded:
            unassigned.append(f"{c['id']} ({pm})")
    for cid, sids in listed.items():
        c = next((c for c in clues if c["id"] == cid), None)
        if c and c["planted"].strip() not in sids:
            warnings.append(f"clue: {cid} is listed in {', '.join(sids)} but the ledger plants it at {c['planted']}")

    # --- report ---
    print(f"Scenes: {len(scenes)}   Words: {total:,}   Interludes: {len(interludes)} ({sum(int(r['words']) for r in interludes):,} words)")
    print("\nMovements (planned / contract):")
    for mv in MOVEMENTS:
        w = sum(int(r["words"]) for r in scenes if r["movement"] == mv)
        if mv not in storyboarded:
            print(f"  {mv:>3}: not yet storyboarded (contract {BUDGET[mv]:,})")
            continue
        flag = "" if abs(w - BUDGET[mv]) <= BUDGET[mv] * 0.1 else "   <-- outside 10%"
        print(f"  {mv:>3}: {w:>6,} / {BUDGET[mv]:,}{flag}")

    hinge = next((s for r, s in zip(scenes, starts) if date_key(r["date"]) >= ANNIVERSARY), None)
    if hinge is not None and total:
        print(f"\nThe anniversary starts at {hinge:,} words ({hinge / total:.0%} of what is storyboarded)")
    else:
        print("\nThe anniversary is not yet storyboarded")

    print("\nPOV share (words, scenes):")
    for pov, spans in sorted(by_pov.items(), key=lambda kv: -sum(e - s for s, e, _ in kv[1])):
        w = sum(e - s for s, e, _ in spans)
        print(f"  {pov}: {w:>6,}  {len(spans):>2}  ({w / total:.0%})")
    if gaps:
        print("\nPOV absences over the limit:")
        for g, pov, a, b in sorted(gaps, reverse=True):
            print(f"  {pov}: {g:,} words between {a} and {b}")

    plants = [c for c in clues if c["kind"] == "plant"]
    print(f"\nClues: {len(clues)} ({len(plants)} plants, {len(clues) - len(plants)} finds)")
    for mv in MOVEMENTS:
        p = [c["id"] for c in clues if movement_of(c["planted"], scene_movement) == mv]
        t = [c["id"] for c in clues if movement_of(c["turns"], scene_movement) == mv]
        print(f"  {mv:>3}: planted or found {len(p):>2}   turn {len(t):>2}")
    if unassigned:
        print("\nClues planted in a storyboarded movement but not yet given a scene: " + ", ".join(unassigned))

    for w in warnings:
        print("WARN", w)
    for e in errors:
        print("FAIL", e)
    print(f"\n{len(errors)} failures, {len(warnings)} warnings, {len(gaps)} long absences")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
