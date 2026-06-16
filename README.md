# no-em-dashes

<img width="1176" height="778" alt="exmergo-no-em-dashes-skill" src="https://github.com/user-attachments/assets/acb2db7a-b5eb-42de-aa90-d38be64ef45d" />


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

## Use with other coding agents

The two-command install above is specific to Claude Code, which has a plugin
marketplace. Most other agents do not install packages; they read **committed
instruction files**. The good news is that one file reaches almost all of them.

### Start here: `AGENTS.md`

This repo ships an [`AGENTS.md`](AGENTS.md), the open standard (now under the Linux
Foundation) that Cursor, GitHub Copilot agent mode, Codex, Continue, Aider, Windsurf,
and others read automatically. To get the behavior in your own project, copy the
contents of our `AGENTS.md` into your repository's `AGENTS.md` (merge if you already
have one). That single step covers the majority of agents, with no install command.

`AGENTS.md` is the canonical source of the guidance. The per-tool files below are thin
pointers to it, so nothing drifts.

### Per-tool files

| Agent | File in this repo | How to adopt |
|-------|-------------------|--------------|
| Cursor | [`.cursor/rules/no-em-dashes.mdc`](.cursor/rules/no-em-dashes.mdc) | Copy into your repo's `.cursor/rules/`, or use **Settings -> Rules -> Remote Rule (GitHub)** and paste this repo's URL to auto-sync. |
| GitHub Copilot | [`.github/copilot-instructions.md`](.github/copilot-instructions.md) | Copy into your repo's `.github/`. |
| Windsurf | [`.windsurf/rules/no-em-dashes.md`](.windsurf/rules/no-em-dashes.md) | Copy into your repo's `.windsurf/rules/`. |

### Two honest caveats

- **Mostly project-scoped.** For these agents you get the rule by placing the file in a
  given project, not by installing it once for everything. The cleanest "applies
  everywhere" options remain the Claude Code plugin above and Cursor's Remote Rules.
- **The checker needs a shell.** The prose guidance works in every agent. The
  `check_em_dashes.py` scan only helps in agents that can run a terminal command (Cursor
  agent mode, Windsurf, Claude Code), and only when the rule tells them to run it.

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
AGENTS.md                          canonical cross-agent guidance (see "Use with other coding agents")
.claude-plugin/
  plugin.json                      Claude Code plugin manifest (name, version, author)
.cursor/rules/no-em-dashes.mdc     Cursor rule, points to AGENTS.md
.github/copilot-instructions.md    GitHub Copilot instructions, point to AGENTS.md
.windsurf/rules/no-em-dashes.md    Windsurf rule, points to AGENTS.md
skills/
  no-em-dashes/                    the Claude Code skill itself
    SKILL.md                       the instructions Claude Code loads
    scripts/check_em_dashes.py     a checker that flags em dashes and stand-ins
    evals/                         test prompts (evals.json) and recorded results
      results/em_dash_counts.csv   em dash counts per eval, with skill vs without
tests/                             standard-library unit tests for the checker
MAINTAINING.md                     release flow, private-to-public, and sync notes
CONTRIBUTING.md  CODE_OF_CONDUCT.md  LICENSE
```

The writing guidance lives in two self-contained files on purpose: `SKILL.md` for
Claude Code and `AGENTS.md` for every other agent. They mirror the same rule because
each ships independently; see [MAINTAINING.md](MAINTAINING.md) for how they stay in sync.

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

Yes. See [`skills/no-em-dashes/evals/results/`](skills/no-em-dashes/evals/results),
including [`em_dash_counts.csv`](skills/no-em-dashes/evals/results/em_dash_counts.csv).
Across five prompts (short marketing copy, a team email, an interrupted-dialogue scene,
a 1000-word essay, and a 1000-word landing page), the skill produced zero em dashes
every time. The skill-free baseline produced them in four of the five, and the count
climbed with length and rhetorical heat: 3 in the email, 5 in the dialogue, 6 in the
essay, and 18 in the landing page.

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
