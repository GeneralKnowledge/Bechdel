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

## Movements II to VI, version 1 (15 Nov 2026)

43 scenes and three interludes, from 2 January to midsummer 1022. With Movement I: 52 scenes, 86,800 words, plus four interludes of 1,200 (91,600 in all, under the 100,000 ceiling). POV share: Tamsin 62%, Perpetua 16%, Kate 12%, Bryony 10%. The anniversary scene (V-02) starts at 62,800 words, 72% of the way through. Every clue is placed at a scene, and each turns at a named scene after it is planted (`turns` in [clues.tsv](../mystery/clues.tsv) now holds scene IDs). The ordinary life in each scene comes from [world/](../world/).

### Epigraphs

| Movement | From | Passage |
|---|---|---|
| I | The Great Life | The opening: Senna at her desk in the Registry, the light on the rolls |
| II | The Great Life | The raiders at the door (the passage that is Hild's) |
| III | The Great Life | The death, the line Honor will make longer |
| IV | Dorcas's Account | "She was made dead for the rolls, and the house of the Keeping was the poorer." |
| V | Dorcas's Account | A plain sentence about the copies |
| VI | Dorcas's Account | Its last line |

The texts are in [canon/documents/](../canon/documents/).

### II. The pattern (2 January to 5 February)

The letter, the cancelled roll, the school record and the meeting-house readings make the Wexham Senna the saint. Pressure: Orla's leak to Fen; the committee; Kate asks Tamsin to stop.

| ID | Date | POV | Scene | Plants or turns |
|---|---|---|---|---|
| II-01 | 2 Jan | Tamsin | The interim report; "a Reading", once, to Juno | |
| II-02 | 6 Jan | Tamsin | The cancelled roll of 644 | C02 turns |
| II-03 | 10 Jan | Kate | Breakfast with Juno; the order of service | C10 "for the rolls" |
| II-04 | 13 Jan | Tamsin | Win Corley and the school record | C03 found and turns |
| II-05 | 15 Jan | Bryony | Fen's column; the sisters' row in the pharmacy | |
| II-06 | 19 Jan | Perpetua | Wednesday lunch: the pupil theory and the Rook theory | |
| II-07 | 27 Jan | Tamsin | Hild's Day at Juno's school | C08 Hild's death |
| II-08 | 30 Jan | Tamsin | The meeting house reads a letter she has on her phone | C04 turns |
| II-09 | 5 Feb | Kate | Kate asks Tamsin to stop | |
| II-X | 645 | Hanne Rusk | Interlude: an errand, a note carried | C29 |

### III. The wrong answer (10 February to 18 March)

The Account, the borrowed death, Honor's lines, the diary and the ink make the relics copies of one winter. Tamsin concludes Senna and Dorcas forged them for the Order, and the Examiner files it. Pressure: Agnes's deadline; Perpetua's report; Kate finds out.

| ID | Date | POV | Scene | Plants or turns |
|---|---|---|---|---|
| III-01 | 10 Feb | Tamsin | Dorcas's Account, at one table with Perpetua | C07 found and turns |
| III-02 | 15 Feb | Perpetua | The copybook; the Great Life beside Hild | C08 turns |
| III-03 | 18 Feb | Tamsin | Honor rehearses; two lines that are not in the book | C09 turns |
| III-04 | 22 Feb | Bryony | The solicitors; the pear row pruned together | |
| III-05 | 25 Feb | Tamsin | Aunt Ros and Marit's diary | C06 turns |
| III-06 | 2 Mar | Tamsin | The dyeworks ink book; the infirmary index | C05 turns; C18 planted |
| III-07 | 6 Mar | Tamsin | The survey room; Agnes's deadline | C27 planted |
| III-08 | 9 Mar | Kate | A night on the ward; Ros's text | |
| III-09 | 11 Mar | Tamsin | The wrong answer, told to Perpetua | |
| III-10 | 14 Mar | Perpetua | The preliminary report | |
| III-11 | 18 Mar | Tamsin | The pass withdrawn; Juno's concert | |
| III-X | 647 | Bett Langley | Interlude: the coins | C30 |

### IV. The missing distinction (21 March to 7 April)

"Made dead" was a sentence. The relics were the trial exhibits; the witness was bought; Benedicta asked for the entries; Dorcas offered restoration and Senna refused; Marit knew. Pressure: Delphine and the housing vote; the translation coming.

| ID | Date | POV | Scene | Plants or turns |
|---|---|---|---|---|
| IV-01 | 21 Mar | Tamsin | Her own photograph disproves her | C27 turns |
| IV-02 | 24 Mar | Perpetua | The tribunal register, the charge sheet, the 690 petition | C10, C11, C12 turn |
| IV-03 | 25 Mar | Bryony | The frost night; the packet | C14 found |
| IV-04 | 26 Mar | Tamsin | The Teague papers, with Delphine | C13, C23 found and turn |
| IV-05 | 29 Mar | Tamsin | Dorcas's offer, Senna's refusal, the letter from M. | C14, C24 turn |
| IV-06 | 1 Apr | Kate | Kate will not hear it before the anniversary | |
| IV-07 | 3 Apr | Perpetua | The report withdrawn; Hesketh will examine the bones | |
| IV-08 | 5 Apr | Tamsin | Marit's petition, under "Consolations of the bereaved" | C15 planted |
| IV-09 | 7 Apr | Tamsin | The joint service; where is she buried? | |
| IV-X | about 900 | The cataloguer | Interlude: filing a petition | C31 |

### V. The causal solution (8 April to 9 May)

The tomb is opened; the bones are contested; Senna's grave is in Wexham; the documents identify Jory. Pressure: the anniversary; Fen's scoop; Hesketh's own expert.

| ID | Date | POV | Scene | Plants or turns |
|---|---|---|---|---|
| V-01 | 8 Apr | Tamsin | Juno's concert | |
| V-02 | 9 Apr | Perpetua | The anniversary; the tomb opened; the first expert | C17 found |
| V-03 | 11 Apr | Bryony | Grandmother Senna's stone | C21 found and turns |
| V-04 | 16 Apr | Tamsin | Fen's scoop and the second expert; the river | C18 turns |
| V-05 | 19 Apr | Kate | "Word from W."; the petition read as hope | C15, C31 turn |
| V-06 | 22 Apr | Tamsin | The kitchen table: Jory | C16, C20, C26, C28 turn |
| V-07 | 28 Apr | Perpetua | Hesketh decides to withdraw the Cause | C17 settles |
| V-08 | 4 May | Tamsin | The city fine; Agnes across the table | C19 found |
| V-09 | 9 May | Tamsin | Tamsin tells Juno everything | |

### VI. The changed world (16 May to midsummer)

The decisions, in the contract's order: Kate, Hesketh and Perpetua, the Rooks, Delphine, the oath, taking Jory in, the space below her name.

| ID | Date | POV | Scene | Plants or turns |
|---|---|---|---|---|
| VI-01 | 16 May | Tamsin | Tamsin tells Kate first | C22 turns |
| VI-02 | 30 May | Perpetua | The Cause withdrawn; Perpetua resigns; Delphine publishes | |
| VI-03 | 6 Jun | Bryony | The orchard settled and not sold | |
| VI-04 | 12 Jun | Tamsin | Jory's life; the oath refused | C19 turns |
| VI-05 | 19 Jun | Kate | The housing vote; taking Jory in | C25 turns |
| VI-06 | 24 Jun | Tamsin | The decree; the copy; the space | |

## Choices in Movements II to VI

Each is built as recommended, so nothing waits on an answer. Each can be changed by editing rows, before drafting.

1. **How the letters reach the paper.** Tamsin's interim report has to cite the letter of 668 as evidence; Orla, who receives the report, gives it to Fen (II-01, II-05). This makes Bryony's misreading cost something, gives Orla a reason the attention pleases her, and leaves Tamsin partly to blame without making her careless. Alternative: Fen finds the letters through the meeting house. **Recommended: Orla.**
2. **Bryony held a packet back.** The plan has Dorcas's offer and Senna's reply "in the bundle from I-05 but unread until IV", which would make Tamsin careless with the most important letters in the box. Instead Bryony kept a tied packet back in December, because her mother kept it apart, and gives it up after the frost night (IV-03). I-05 is unchanged; her lens in II-05 and III-04 shows the reader she is hiding something. **Recommended.**
3. **How Tamsin gets back into the archives after losing her pass.** Perpetua takes her in on the Examiner's warrant (IV-02, IV-08), which turns the woman who filed Tamsin's wrong answer into her ally and gives Perpetua a risk of her own. **Recommended.**
4. **Senna's grave before the tomb is solved.** Bryony shows Tamsin and Perpetua the Wexham stone two days after the tomb is opened (V-03), before the documents identify Jory (V-06). The order makes "if Senna is here, who is in Calloway?" an open question for a scene, rather than a footnote to the answer. **Recommended.**
5. **Tamsin tells Juno before Kate.** The contract has Tamsin tell Kate "first, before anyone official". Juno lives with her and learns it at the kitchen table (V-06, V-09); Kate is the first person she tells on purpose (VI-01). **Recommended**; the alternative is to keep Juno in the dark until VI, which would make the household roll in VI-05 harder to believe.
6. **Hesketh concedes the letters in IV-07**, the "point to the sceptic" in [theories.md](../mystery/theories.md), on the meeting house's centuries-old reading copies rather than on a laboratory test. Science never settles anything alone. **Recommended.**
7. **Delphine is not a POV and gets no scene of her own after IV-04.** Her choice is seen from Perpetua's seat in the gallery (VI-02) and on the ward radio (VI-05). **Recommended**, to keep the POVs to four; the alternative is a short Tamsin scene with Delphine in VI.

## Carried into drafting

- The interludes never name Senna, Benedicta, Carrow or Marit, and Jory's never says where she will be buried.
- The second layer has five plants before V: the alms book (I-03), the tomb's inscription (I-07), the porch woman in Marit's diary (I-08), the soup (I-X) and the infirmary entry (III-06). The Movement I and III questionnaires test whether they are too loud.
- Tamsin says "a Reading" once, in II-01.

## Next

The blind voice pilot ([pilot/README.md](../pilot/README.md)): the packet is ready in project files. Then drafting, movement by movement.
