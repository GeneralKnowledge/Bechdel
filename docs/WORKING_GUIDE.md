# Working guide

How the plan, canon, storyboard and drafts fit together, and how work on the book is done. The method is the one Reuben's *Ides of March* project settled on for its Books 2 and 0; [LESSONS_FROM_IDES.md](LESSONS_FROM_IDES.md) says where each part came from.

## Source of truth (read in this order)

1. **The contract**, [CONTRACT.md](../CONTRACT.md). Decisions only Reuben changes.
2. **Canon**, [canon/](../canon/) and [mystery/](../mystery/). What happened in 645 to 1022, which document each event left, who everyone is, how the Keeping works, every clue and theory. Where canon and the plan doc differ, canon wins; record the difference in the changelog.
3. **Storyboard**, [storyboard/scenes.tsv](../storyboard/scenes.tsv). What happens in which scene, in what order.
4. **Voice**, [voice/MIND_SHEETS.md](../voice/MIND_SHEETS.md) and [voice/WATCHLIST.md](../voice/WATCHLIST.md).
5. **Drafts**, [draft/](../draft/), once they exist. Authoritative for what is written.
6. **The plan doc**, [The Grave Signed with Her Hand: Revised Story Plan](https://claude.ai/artifact/R7xyPomX2ZuymeQyya4d7a). The reasoning behind the story and the comparable-novels lessons. Read it for *why*; read canon for *what*.

| Question | File |
|---|---|
| What has Reuben decided? | [CONTRACT.md](../CONTRACT.md) |
| What really happened, and what document did it leave? | [canon/chronology.md](../canon/chronology.md) |
| Who is this, and what is she called on the page? | [canon/names.md](../canon/names.md) |
| How does the faith work? | [canon/faith.md](../canon/faith.md) |
| Where does each clue live, and when does its meaning turn? | [mystery/clues.tsv](../mystery/clues.tsv) |
| Which theories are live, and what stays open? | [mystery/theories.md](../mystery/theories.md) |
| What happens in this scene? | [storyboard/scenes.tsv](../storyboard/scenes.tsv) |
| How does this woman think? | [voice/MIND_SHEETS.md](../voice/MIND_SHEETS.md) |
| What to check when a movement is drafted | [voice/WATCHLIST.md](../voice/WATCHLIST.md) |
| What readers have said | [reader_feedback/OPEN_CRITICISMS.md](../reader_feedback/OPEN_CRITICISMS.md) |

## Stages

| Stage | Done when |
|---|---|
| 0. Plan | Reuben has answered the plan's checklist (done 23 Oct). |
| 1. Contract | Reuben approves it. |
| 2. Canon pack | Chronology, names, places, faith, clue ledger and theories agree with each other and with the contract, and both checks pass. |
| 3. Mind sheets and storyboard | Every POV and every document voice has a sheet. The whole book is storyboarded, the storyboard check passes, and Reuben has picked among its choices. Each movement has a questionnaire and key. |
| 4. Blind voice pilot | Passes the test set in [pilot/README.md](../pilot/README.md). If it fails, fix the mind sheets, not the scenes, and rerun once with fresh scenes. |
| 5. Draft by movement | Each movement drafted once at full length, then self-audited (below). |
| 6. Readers, structure audit, freeze | One outside reader per movement on a stamped copy with that movement's questionnaire; then a structure audit; then one whole-book cold read with nothing protected; then one correction round. |

**No prose until the storyboard and the pilot pass.** Short in-world documents (a diary entry, a tribunal formula, a hymn verse) may be drafted earlier when a storyboard row needs their exact wording, because the wording is a clue. They go in [canon/documents/](../canon/documents/) and are canon once written.

## Drafting and self-audit

Draft a movement once at full length from the storyboard and the mind sheets. Then, once per movement:

1. **The three tests** on every scene: action (what happens and what changes), point of view (what would this woman notice, misread, hide), explanation (is the narration telling the reader what the scene has shown).
2. **The two ending tests**: take the last sentence away; end on the action instead.
3. **The watchlist**, [voice/WATCHLIST.md](../voice/WATCHLIST.md).
4. **Fair play**: every clue the storyboard says this movement plants is on the page, and no clue turns before it was planted. `python3 tools/storyboard_check.py`.
5. **Document length**: no in-world document longer than a page.

Record what changed in one changelog line for the movement, with a short list of things to check in the movement's README.

## Changing the book later

**Development** (new scene, moved turning point, new thread) needs: a named story need; a scene with a POV who wants something and leaves changed, not a report; a plant or a payoff; canon and the contract intact; never length for its own sake. Add the row to the storyboard first.

**Revision** (changing prose that exists) needs a demonstrated defect: where, what the reader experiences, why it fails, the smallest fix, and its side effects on voice, ambiguity and later payoffs. A reviewer who can only say "a rule says so" has not shown a defect. Cutting a line that restates what the scene has just shown needs only a note of what it repeats.

**Reader notes** are triaged before anything is touched:

| Class | Means | Action |
|---|---|---|
| Defect | A factual, continuity, clarity or story problem you can show in the text | Fix |
| Reader response | A real reaction that may or may not need a change | Weigh: is this the reaction the scene intends? |
| Preference | A suggestion that would make the book different, not better | Note it; reject if it cuts against the contract |

Then one correction round, checking only the changed passages and what depends on them. Criticisms not acted on go in [reader_feedback/OPEN_CRITICISMS.md](../reader_feedback/OPEN_CRITICISMS.md) and are counted by source.

## Records

- One changelog line per change, in the README. No pass logs.
- Scene IDs (I-01, II-04...) are permanent. Chapter numbers are assigned only at export.
- A new named person gets a row in [canon/names.md](../canon/names.md) before she appears in a scene.
- A new document gets a row in [canon/chronology.md](../canon/chronology.md); a new clue gets a row in [mystery/clues.tsv](../mystery/clues.tsv).
