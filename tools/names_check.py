#!/usr/bin/env python3
"""Check canon/names.md: one handle, one person.

Reads the first two columns (Handle, Also on the page) of every person table.
Fails if a name is used for two people (case-insensitive), or if a name on
the "Retired names" line is used again.

Also prints, as warnings only, pairs of names across different people that
are close enough to confuse a reader: an edit distance of 1, or 2 when either
name has six letters or more. Names shared within a family (Aldous, Rook) are
not flagged. Warnings never fail the check, and the script does NOT read the
Near column in names.md: whether each pair is recorded there, and what is
done about it, is checked by a person.

Usage: python3 tools/names_check.py
"""
import sys
from itertools import combinations
from pathlib import Path

NAMES = Path(__file__).resolve().parent.parent / "canon" / "names.md"
SKIP_TITLES = {"mother", "sister", "keeper", "saint", "councillor", "aunt", "the", "of", "registrar-general"}


def distance(a, b):
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        cur = [i]
        for j, cb in enumerate(b, 1):
            cur.append(min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (ca != cb)))
        prev = cur
    return prev[-1]


def main() -> int:
    people = []  # (handle, set of names)
    in_people_table = False
    for line in NAMES.read_text(encoding="utf-8").splitlines():
        if line.startswith("| Handle"):
            in_people_table = "Also on the page" in line
            continue
        if not line.startswith("|"):
            in_people_table = False
            continue
        if line.startswith("|---") or not in_people_table:
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        handle, also = cells[0], cells[1]
        names = {handle} | {a.strip() for a in also.replace(";", ",").split(",") if a.strip()}
        people.append((handle, names))

    failures = 0
    owner = {}
    for handle, names in people:
        for n in names:
            key = n.lower()
            if key in owner and owner[key] != handle:
                print(f"DUPLICATE name {n!r}: used for {owner[key]!r} and {handle!r}")
                failures += 1
            owner[key] = handle

    import re
    m = re.search(r"Retired names:\s*(.+?)\.", NAMES.read_text(encoding="utf-8"))
    retired = {w.strip().lower() for w in m.group(1).split(",")} if m else set()
    for handle, names in people:
        for n in names:
            for w in n.split():
                if w.strip(",.").lower() in retired:
                    print(f"RETIRED name {w!r} used for {handle!r}")
                    failures += 1

    # words that could be read alone on the page (given names, surnames)
    words = {}
    for handle, names in people:
        for n in names:
            for w in n.replace("*", "").split():
                w = w.strip(",.").lower()
                if len(w) >= 4 and w not in SKIP_TITLES and w[0].isalpha():
                    words.setdefault(w, set()).add(handle)
    near = []
    for a, b in combinations(sorted(words), 2):
        if words[a] & words[b]:
            continue
        d = distance(a, b)
        if d <= (2 if max(len(a), len(b)) >= 6 else 1):
            near.append((d, a, b, sorted(words[a])[0], sorted(words[b])[0]))
    for d, a, b, ha, hb in sorted(near):
        print(f"WARN near: {a.title()} ({ha}) ~ {b.title()} ({hb})  distance {d}")
    print(f"\n{len(people)} people, {failures} failures, {len(near)} near-name warnings"
          " (not checked against the Near column)")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
