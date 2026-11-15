# What building the canon and storyboard found in the plan

Putting the plan into a contract, a chronology, a names table, a clue ledger and a Movement I storyboard, and running the two checks over them, turned up the following. Most important first. None needs the story to change; most are a name or a line.

**Short answer:** three names are close enough to confuse a reader and are worth changing before any drafting (items 1 to 3). Two mechanics need one sentence of canon each (items 5 and 6). The second layer (the tomb holds Jory) had too few early plants in the plan's ledger; the storyboard adds them, for Reuben to approve (item 8). The interludes can do fair-play work if they are ordered for it (item 7).

## Decisions (Reuben, 15 Nov 2026, review of PR #1)

| # | Decision | Done in |
|---|---|---|
| 1 | Merrit renamed **Ada** | `canon/names.md`, `canon/chronology.md` |
| 2 | Perpetua Vane renamed **Perpetua Gaunt** | `canon/names.md` |
| 3 | Win Haskett renamed **Win Corley** | `canon/names.md`, `voice/MIND_SHEETS.md`, `mystery/clues.tsv` |
| 4 | Bett Langley and Benedicta Teague both kept: the likeness allows one fair misreading of "B. L." | `canon/names.md` |
| 6 | Approved: the Teagues wanted Wexham's eastern land, which went back to the Wexham smallholders in 649 | `canon/chronology.md`, `canon/places.md` |
| 8 | C26 approved with a refinement: the diary line must not mention the leg, the vats or a name. Jory should be available to the reader, not salient | `mystery/clues.tsv`, `storyboard/scenes.tsv`, `canon/documents/README.md` |

| 5 | Senna's fair copy of her reply to Dorcas is canon. Dorcas sends the offer to Wexham; Senna refuses on those terms and keeps a fair copy, which reaches the Rook box. The letters are an exchange between two women, not an explanation for a future reader | `canon/chronology.md` |
| 7 | Four interludes: Jory after I, Hanne Rusk after II, Bett after III, the cataloguer after IV, none after V; Jory does not return | `CONTRACT.md`, `storyboard/README.md`, `mystery/clues.tsv` |
| 9 | Kate's reading of Marit is a family disagreement with Aunt Ros, who has a real case; it begins at the Reading in I-08 and Marit's motive is never resolved | `storyboard/scenes.tsv` (I-08), `voice/MIND_SHEETS.md`, `mystery/theories.md`, `canon/names.md` |
| 10 | Tamsin's "a Reading" is kept: said once, to Juno, in the first Tamsin scene after I-08; never a catchphrase; the narration never uses it in her sense | `voice/MIND_SHEETS.md`, `storyboard/README.md` |
| 12 | Marit's mother owned a modest dyeworks; Marit worked there from girlhood and knew Jory. Her mother has no further part | `canon/chronology.md`, `canon/names.md`, `canon/places.md` |

Second set, 15 Nov (Reuben, after the second commit): items 5, 7, 9, 10 and 12 above. Every finding is now settled except 13, which is a watch item; item 11 was settled with the calendar (storyboard choice 3).

## Findings

| # | Finding | Severity | Recommendation |
|---|---|---|---|
| 1 | **Marit and Merrit.** Senna's hearth partner and the daughter Senna had in Wexham differ by two letters, and both turn up in the letters and the diary in Movements IV and V, often in the same paragraph. `tools/names_check.py` flags it. | Medium | Rename the daughter. Anything that does not start with M and is not close to Marit, Wren or Tobi: for example **Ada**. |
| 2 | **Perpetua Vane and Oriel Vance.** The Examiner spends Movement III examining the Great Life by its author. "Vane found that Vance..." will happen. | Medium | Change Perpetua's surname, for example **Perpetua Gaunt**. Oriel Vance is mostly "Keeper Vance" or "the author of the Great Life". |
| 3 | **Hesketh and Haskett.** Mother Hesketh Lorne and Win Haskett, keeper of the Wexham school records. Win appears in II and V, when Hesketh is in most scenes. | Low to medium | Change Win's surname, for example **Win Corley**. |
| 4 | **Bett and Benedicta.** Bett is a short form of Benedicta, and both are in the 647 tribunal and the Teague papers. The steward's "B. L., for her word" could be read once as Benedicta. | Low; possibly useful | Keep, and use it: Delphine (or Fen) reads "B." as Benedicta in IV before the tribunal record names Bett Langley. If not wanted, rename Bett. |
| 5 | **Senna's reply to Dorcas is in the Rook box.** A letter Senna sent would be in Dorcas's papers, not Senna's. | Low | Senna kept a fair copy of her reply, which is her habit as a copyist and is in character. Added to the chronology as a choice. |
| 6 | **How a Wexham orchard is among the Teague entries.** The 668 letter describes the Rook orchard's boundary as the forged entry had it, so the orchard was one of the entries Carrow altered for the Teagues, and Bryony's orchard is finally settled "on the corrected roll". The plan does not say why the Teagues wanted Wexham land. | Medium | Wexham lies east of Calloway, and Benedicta's note asks for "the eastern entries". After the 649 judgment the land went back to the Wexham smallholders, Lise Rook's household among them. This also gives Senna a reason Wexham's people would take her in without papers. **Reuben to approve**: it adds a motive to Senna's choice of Wexham. |
| 7 | **The interludes can carry fair play.** Several clues turn in IV with nothing planted earlier (the steward's payment, Benedicta's note). | Medium | Order the five interludes so each plants what the next movement turns, without naming anyone: after I, **Jory** (the soup); after II, **Hanne Rusk** (an errand for her mistress, a note carried); after III, **Bett** (the day she took the money); after IV, **the cataloguer** (the petition she files); after V, none, or Jory again, briefly. |
| 8 | **The second layer had too few early plants.** The plan's guardrail says to plant Jory "in Marit's diary and the alms book early", but its ledger has no diary entry about Jory and turns the alms book only in V. The storyboard adds a diary line about the woman on the chapel porch (C26, read at the Reading in I-08), the alms book in a chapel case (C20, I-03) and the soup in Jory's interlude (C28). | Medium | Approve C26. The diary line's exact words are a clue and should be drafted before I-08; it goes in `canon/documents/`. The Movement I questionnaire tests whether the plants are too loud. |
| 9 | **Kate "refuses both" readings of Marit.** On *Ides*, a reader flagged secondary characters handed the sentence that explains the lead ("Horace's father's freedom explains Brutus's mercy"). Kate's line risks being the book's verdict on Marit. | Low | Kate is a POV in the proposed contract, so stage it as her family's quarrel, with Aunt Ros on the other side, not as a summing-up. Watchlist question 8. |
| 10 | **"Reading" means two things.** The plan has Tamsin coin the word "a Reading" for a story everyone repeats without checking, and the Reading is also the household ritual. | Low | Keep the pun, which is good, but let Tamsin say it aloud once, to Juno, after I-08; the narration never uses it in that sense. Or choose another word for the coinage. |
| 11 | **No season or date for 1022.** The plan dates the present only to the year. | Low; needed for the storyboard | Storyboard choice 3: anniversary on 9 April 1022; the Reading on the last night of the year; the book from mid-December 1021 to midsummer 1022. |
| 12 | **Jory and Marit's dyeworks.** Jory broke her leg at a dyeworks in 631, "possibly Marit's"; Marit was about 19 in 631. | Very low | The dyeworks was Marit's mother's, and Marit worked in it. That is how she knows the porch woman (C26). |
| 13 | **The "kept" motif.** The faith's central word will be in every scene. On *Ides*, "debt" reached saturation and readers said so. | Watch | Watchlist question 6. |

## Checked and fine

- 1022 is the 375th anniversary of 647; the letter dated 668 is 21 years after it.
- Senna was 31 in 647, and Jory about 60; the bones (about sixty, a badly healed break) and Hesketh's expert's wrong reading ("a thirty-one-year-old with a hard life can look older") both hold.
- Wren is 7 in 647 and 21 when Marit writes "Wren has your hand" in 661.
- The meeting house has read the letters since the 700s, about three hundred years before 1022.
- Every clue in the plan's ledger turns no earlier than it can be found. `tools/storyboard_check.py` now checks this on every change.
