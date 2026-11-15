# The Grave Signed with Her Hand

*A novel of the Thousand-Year World*

by Reuben Dennison

---

Every year the city of Calloway reads aloud the Life of Senna Aldous, the registrar who died for the rolls in 647. The rolls she saved hang in the Registry Chapel, and the chapel tomb is believed to hold her body. In the 375th year after her death, the Order of Keepers is ready to make her a saint.

Tamsin Hale, a title researcher who once swore her keeper's oath "by Senna's rolls", takes a dull job in the town of Wexham: two sisters, not speaking, fighting over the boundary of an orchard. The younger sister produces a bundle of family letters to settle it. They are signed "Senna" and dated 668, twenty-one years after the saint's death. In the margins is a small hooked correction stroke that Tamsin has looked at every working day of her career.

The record is true. Only its meaning is wrong.

---

This repository is the working home of the novel: its plan, canon, storyboard, voice notes and, later, its drafts. The working story plan is the doc [The Grave Signed with Her Hand: Revised Story Plan](https://claude.ai/artifact/R7xyPomX2ZuymeQyya4d7a). From this repository's first PR on, the files here are the source of truth, and the plan doc is the record of how the story was chosen.

How the work is organised, and why, is in [docs/WORKING_GUIDE.md](docs/WORKING_GUIDE.md). What was borrowed from the *Ides of March* project, and what was deliberately left behind, is in [docs/LESSONS_FROM_IDES.md](docs/LESSONS_FROM_IDES.md).

## Where things stand

| Stage | What | Status |
|---|---|---|
| 0 | [Story plan](https://claude.ai/artifact/R7xyPomX2ZuymeQyya4d7a) and Reuben's answers to its checklist | Done, 23 Oct 2026 |
| 1 | [Contract](CONTRACT.md) | Approved by Reuben, 15 Nov 2026 |
| 2 | Canon pack: [chronology](canon/chronology.md), [names](canon/names.md), [places](canon/places.md), [the Keeping](canon/faith.md); mystery: [clue ledger](mystery/clues.tsv), [theories and what stays open](mystery/theories.md) | First version, from the plan |
| 3 | [World](world/README.md), [mind sheets](voice/MIND_SHEETS.md), [watchlist](voice/WATCHLIST.md), [storyboard](storyboard/README.md), [questionnaire](storyboard/questionnaire.md) | Whole book storyboarded: 52 scenes and four interludes, about 91,600 words; questionnaire and key for every movement. Seven choices in Movements II to VI built as recommended, for Reuben |
| 4 | [Blind voice pilot](pilot/README.md) | Passed on two cold reads by fresh Claude readers, 15 Nov 2026; a person's read still to come |
| 5 | Draft by movement | [Movement I](draft/movement1/README.md) drafted and self-audited (13,478 words and Jory's interlude); II to VI not started |
| 6 | Structure audit, cold read, freeze | Not started |

Findings from building stages 1 to 3, with Reuben's decisions and what is still open: [docs/PLAN_FINDINGS.md](docs/PLAN_FINDINGS.md). What comes next: [docs/ROADMAP.md](docs/ROADMAP.md). The world as it would be without the mystery: [world/](world/README.md).

## Checks

```
python3 tools/storyboard_check.py   # dates, POV gaps, movement budgets, where the anniversary falls, clue fair play
python3 tools/names_check.py        # one handle, one person, retired names; near pairs printed as warnings only
```

Both run on every pull request.

## Changelog

One line per change.

- 2026-11-15: Repository set up from the plan, using the method learnt on *The Ides of March* (Books 2 and 0). Contract draft, canon pack, clue ledger and theories, mind sheets, watchlist, Movement I storyboard v1 with questionnaire and key, plan findings, check tools and CI.
- 2026-11-15: Reuben's review of PR #1. Contract approved; storyboard choices settled as recommended; Merrit renamed Ada, Perpetua Vane renamed Perpetua Gaunt, Win Haskett renamed Win Corley; Bett and Benedicta kept; Wexham's eastern land approved; C26 approved without the leg, the vats or a name; README no longer states that Senna lies in the tomb; manual clue verification added to the working guide; names check reports near pairs as warnings and fails on retired names; roadmap added.
- 2026-11-15: Reuben settled the last five findings: Senna's fair copy of her reply is canon; four interludes (Jory, Hanne, Bett, the cataloguer, none after V); Kate and Aunt Ros disagree about Marit as family, from I-08, motive unresolved; "a Reading" said once to Juno after I-08, never in narration; Marit's mother owned the dyeworks and Marit knew Jory. C16 corrected to I-07 in theories; stale scene IDs in the faith file corrected.
- 2026-11-15: The book built to the pilot. World bible added (`world/`: the year, money, Calloway, Wexham, the cast's ordinary lives, a relationship map). Movements II to VI storyboarded (43 scenes, three interludes, every clue placed at a scene and turned at a later one; three new interlude clues C29 to C31; C04 now turns in II, C14's packet is one Bryony held back). Chronology gains the 1022 calendar, the cancelled roll and the ink book; the orchard boundary fixed in places. Six canon documents written (Marit's diary, two Senna letters, Hild, the Great Life's death with Honor's lines, the Account; the epigraphs). Tobi corrected from Marit's son to her daughter. Bea and Nell added to names. Questionnaires and keys for II to VI. Pilot packet built in project files.
- 2026-11-15: Voice pilot passed on two cold reads (Reuben chose a fresh Claude read now, a person later); fixes the readers showed made in I-05 and I-08; Marit's and Senna's wit separated in the mind sheets. Movement I drafted in full with its self-audit and clue table; Gilmour's added to names.
