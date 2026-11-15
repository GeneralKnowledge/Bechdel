# Working on this repository

This is a novel, *The Grave Signed with Her Hand*. Read [docs/WORKING_GUIDE.md](docs/WORKING_GUIDE.md) before any change; it gives the source-of-truth order and the stages.

- The [contract](CONTRACT.md) is Reuben's. Do not change a Settled row; propose changes to Proposed rows in the PR or the thread.
- Canon (`canon/`, `mystery/`) wins over the plan doc. New person: a row in `canon/names.md` first. New clue: a row in `mystery/clues.tsv`. New scene: a row in `storyboard/scenes.tsv`.
- No prose until the storyboard and the voice pilot pass.
- Run `python3 tools/storyboard_check.py` and `python3 tools/names_check.py` before committing. CI runs both.
- One changelog line per change, in the README. No pass logs.
- Author voice: British English, no em dashes, no caption fragments, no narrator explaining what a scene has shown. Never explain the absence of men.
