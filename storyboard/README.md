# Storyboard

`scenes.tsv` has one row per scene: ID, movement, date, place, POV, what happens, what changes, what the reader must know by the end, the POV lens (what she notices, misreads and hides), word budget, the scenes it depends on, the clues it plants or turns (IDs from [mystery/clues.tsv](../mystery/clues.tsv)), and the outside pressure it carries. Scene IDs are permanent; chapter numbers are assigned only at export. Interludes have IDs ending `-X` and are dated in their own century.

```
python3 tools/storyboard_check.py
```

The check fails on date rewinds, static scenes, bad dependencies and any clue that turns before it is planted.

## Movement I, version 1 (15 Nov 2026)

Eight scenes, 14,100 words (contract budget 14,000), and one interlude of 1,200. From 14 to 31 December 1021. Opens on the orchard (the plan's guardrail: the quarrel before the faith). Ends at the Reading on the last night of the year, which begins the anniversary year.

POV share: Tamsin 8,800 (5 scenes), Kate 2,200 (1), Perpetua 1,600 (1), Bryony 1,500 (1).

Plants: thirteen clues are planted or found in Movement I, and only one turns there (the stroke itself). All four plants for the second layer that belong in Movement I are placed, each as one item among others: the alms book in the chapel (I-03), Marit's line about the porch woman (I-08), the tomb inscription (I-07), Jory's interlude (I-X).

Outside pressures: Orla's buyer and date; Fen's first column; Juno's rehearsals and her question; Agnes's condition on Tamsin's access; Bryony's week; the Cause's timetable.

| ID | Date | POV | Scene | Plants |
|---|---|---|---|---|
| I-01 | 14 Dec | Tamsin | The orchard boundary, with two sisters not speaking | |
| I-02 | 14 Dec | Tamsin | Juno at the piano; Fen's column; the question about a child | C22 hymn |
| I-03 | 16 Dec | Tamsin | The search room and the chapel; Agnes | C05 relic ink, C20 alms book |
| I-04 | 18 Dec | Bryony | The meeting house reading; the family box | C04 meeting-house letters |
| I-05 | 19 Dec | Tamsin | The bundle on the kitchen table; the stroke | C01 stroke, C02 boundary, C24 letter from M. |
| I-06 | 20 Dec | Perpetua | The Cause opens; Honor rehearses; lunch with Hesketh | C09 Honor's lines |
| I-07 | 22 Dec | Tamsin | After hours in the chapel; the choir; the tomb | C16 "the grave signed with her hand" |
| I-08 | 31 Dec | Kate | The Reading | C06 "tired and secret", C25 taking in, C26 the woman on the porch |
| I-X | 647 | Jory | Interlude: the porch | C28 the soup |

## Choices

**Settled by Reuben, 15 Nov 2026** (review of PR #1): all five as recommended. Four POVs, with Tamsin dominant and a secondary scene only where it shows what she cannot; Perpetua for the Cause; opening 14 December 1021, the Reading on 31 December, the anniversary on 9 April 1022; Movement I ends with Kate; Fen's column stays in I-02, and Movement II gets no extra epigraph for now.

1. **Point of view.** Tamsin plus three secondary POVs (Kate, Perpetua, Bryony), as proposed in the [contract](../CONTRACT.md). The plan says the ensemble's lives "go on without her" and names Hesketh and Perpetua's scenes as "a quiet spine", which needs scenes Tamsin is not in. Alternative: Tamsin only, with the ensemble seen through her; I-04, I-06 and I-08 would become Tamsin scenes or be cut. **Recommended: four POVs.**
2. **Whose eyes for the Cause.** Perpetua rather than Hesketh, because doubt is the more useful lens for a reader and Hesketh's arc (her own examination condemns her Cause) lands harder seen from outside. **Recommended.**
3. **The calendar.** The plan dates the book "1022" without a season. Proposed: the sentence was read on 9 April 647, so the anniversary is 9 April 1022; the household Reading is on the last night of the year; Movement I runs through December 1021 and ends at the Reading, which opens the anniversary year; the anniversary falls in Movement V. This gives the investigation a fixed clock, as the Ides did for the *Ides* books. Alternative: the Reading at midsummer and the book inside 1022 only, which would move I-08 out of Movement I and leave taking in unplanted until later. **Recommended: the December opening.**
4. **I-08 ends Movement I on Kate, not Tamsin.** The Reading is where the plan says Kate's faith is most persuasive, and Kate's misreading of Tamsin's silence is the first consequential misreading in the book. **Recommended.**
5. **A Fen column as a document in Movement I.** Not storyboarded as its own row; it appears on the table in I-02. Alternative: open Movement II with it as an epigraph beside the Great Life. **Settled: not for now.** The Great Life and the Account already carry the epigraphs, and not every movement should feel like a documentary presentation.

## Next

Movement II storyboard, then III to VI, each with its questionnaire and key. Then the blind voice pilot ([pilot/README.md](../pilot/README.md)).
