# no-em-dashes

A [Claude Code](https://code.claude.com/docs/en/skills) skill that produces writing
with zero em dashes, and, just as important, writing built out of sentences that never
reach for one in the first place.

Heavy em-dash use has become one of the most recognizable fingerprints of
machine-written text. Many readers now skim a dash-laden paragraph and think "a bot
wrote this." This skill keeps prose reading as a person's, and it forces tighter,
more deliberate sentences along the way.

Built and shared in the open by [Exmergo](https://www.exmergo.com), the team building
AI agents for data analytics. See more of our work at
[exmergo.com/open-research](https://www.exmergo.com/open-research).


## Install

### Option 1: As a plugin (recommended)

This skill is published through the [Exmergo Skills](https://github.com/exmergo/exmergo-skills)
marketplace. Add the catalog once, then install the skill. Inside Claude Code:

```
/plugin marketplace add exmergo/exmergo-skills
/plugin install no-em-dashes@exmergo-skills
```

The skill then loads automatically and runs whenever Claude writes or edits prose for
you. To update later, run `/plugin marketplace update exmergo-skills`.

### Option 2: Manual copy

If you would rather not use the plugin system, copy the skill folder into your skills
directory:

```bash
git clone https://github.com/exmergo/skill-no-em-dashes
cp -r skill-no-em-dashes/skills/no-em-dashes ~/.claude/skills/   # personal, every project
# or, project-scoped:
cp -r skill-no-em-dashes/skills/no-em-dashes .claude/skills/
```

Claude Code auto-discovers any folder containing a `SKILL.md`. Either way, you do not
have to mention em dashes; clean output is the default.


## What it does

When the skill is active, any prose Claude writes or edits comes out free of:

- the em dash itself (`U+2014`),
- and its disguises: a double hyphen (`word--word` or ` -- `), a hyphen padded with
  spaces (` - `), a stray en dash between words, and the horizontal bar.

The point is not to swap one dash character for a look-alike. It is to recognize the
sentence shape that wanted the dash, then rewrite with real punctuation: a comma,
semicolon, colon, period, or parentheses. The skill includes a playbook for each job
an em dash typically does (the dramatic reveal, the "not just X but Y" pivot, the
interruptive aside, joined clauses, the summary dash, and interrupted dialogue) with
worked before-and-after examples.

It deliberately leaves legitimate hyphens alone: compounds like `well-known` and
`state-of-the-art`, number and date ranges like `10-20` and `2019-2024`, and hyphens
in code, file paths, URLs, and math.

## Repository layout

```
.claude-plugin/
  plugin.json                  plugin manifest (name, version, author)
skills/
  no-em-dashes/                the skill itself
    SKILL.md                   the instructions Claude loads
    scripts/check_em_dashes.py a checker that flags em dashes and stand-ins
    evals/                     test prompts and recorded results
tests/                         unit tests for the checker
```

## The checker

The bundled checker is a single dependency-free Python script. Use it on a file or
through standard input:

```bash
python skills/no-em-dashes/scripts/check_em_dashes.py path/to/draft.txt
echo "Your text here" | python skills/no-em-dashes/scripts/check_em_dashes.py
```

It prints every hit with its line, column, and a suggested fix, and it exits with a
nonzero status if anything is found, so you can wire it into a pre-commit hook or CI
step. It skips fenced code blocks, inline code, and URLs so it does not flag the
hyphens that belong there.

## Does it work?

Yes. See [`skills/no-em-dashes/evals/results/`](skills/no-em-dashes/evals/results) for
the first evaluation pass. Across three realistic prompts, the plain-model baseline
produced em dashes in two of them (including five in an interrupted-dialogue scene, the
hardest case), while the skilled version came out clean every time and still read
naturally.

## Running the tests

The checker has a standard-library test suite (no dependencies):

```bash
python -m unittest discover tests
```

## Contributing

Contributions are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md) for how to propose
changes, and please keep your own prose and commit messages em-dash free (the checker
will tell you if you slip).

## License

[MIT](LICENSE).
