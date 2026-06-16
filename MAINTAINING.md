# Maintaining and releasing

This repo is a single Claude Code plugin (`no-em-dashes`). It is **not** a marketplace.
It is distributed through Exmergo's catalog repo,
[`exmergo/exmergo-skills`](https://github.com/exmergo/exmergo-skills), whose
`marketplace.json` references this repo via a `github` source. Users add that catalog,
not this repo, then install the skill from it.

## Repository layout

```
.claude-plugin/
  plugin.json          plugin manifest: name, version, author, repository
skills/
  no-em-dashes/        the skill (SKILL.md, scripts/, evals/)
AGENTS.md              canonical cross-agent guidance (Cursor, Copilot, Windsurf, ...)
.cursor/ .github/ .windsurf/   per-tool rule files that point to AGENTS.md
tests/                 standard-library unit tests for the checker
```

## Keeping the guidance in sync

The actual writing guidance lives in two self-contained files on purpose:

- `skills/no-em-dashes/SKILL.md` for Claude Code (it needs YAML frontmatter for
  triggering, can be longer because it loads on demand, and calls the checker via
  `${CLAUDE_SKILL_DIR}`).
- `AGENTS.md` for every other agent (always-on context, so it is deliberately leaner
  and assumes no skill runtime).

Neither can point at the other, because each travels alone: a skill is copied as a
self-contained folder, and `AGENTS.md` is copied into other people's repos by itself.
So the core rule (the banned constructs, the replacement playbook, the
do-not-overcorrect list) is intentionally mirrored in both.

The trade-off we accepted: when you change the rule itself, edit **both** files in the
same commit. The dogfood check guarantees neither file introduces an em dash, but it
cannot tell you the two have drifted in wording, so that part is on the author. The
per-tool files under `.cursor/`, `.github/`, and `.windsurf/` are thin pointers to
`AGENTS.md` and do not need editing when the rule changes.

## How users install

Through the catalog (see [`exmergo/exmergo-skills`](https://github.com/exmergo/exmergo-skills)):

```
/plugin marketplace add exmergo/exmergo-skills
/plugin install no-em-dashes@exmergo-skills
```

To pull later changes, a user runs `/plugin marketplace update exmergo-skills`.

## First-time publish

1. Create the repo at `github.com/exmergo/skill-no-em-dashes`.
2. Push this code to the `main` branch (the catalog's `github` source reads the default
   branch unless it pins a `ref`):

   ```bash
   git add -A
   git commit -m "Release no-em-dashes <version>"
   git remote add origin git@github.com:exmergo/skill-no-em-dashes.git
   git push -u origin main
   ```

3. Make sure this repo is listed in the catalog's `marketplace.json`. It already is, so
   once both repos are pushed the install commands above resolve.

Push order matters the first time: push this repo before the catalog (or before anyone
runs the catalog install), so the `github` source has something to resolve.

## Private first, public later

You can ship privately to the team, then open up with no repackaging.

- **While private:** each teammate needs read access to this repo (and to the catalog
  repo) plus working git auth (SSH keys or `gh auth login`). Rule of thumb: if their
  `git clone git@github.com:exmergo/skill-no-em-dashes.git` works in a terminal, the
  catalog install will resolve this skill too.
- **Going public:** change the repo visibility in GitHub settings. Nothing in the repo
  changes and existing installs keep working.
- **Before going public:** scrub the git history for secrets, since public exposes
  every past commit, not just the current files.

## Cutting a release (any change after the first publish)

Updates are version-gated: because `plugin.json` sets a `version`, users only receive
changes when you bump it.

1. Make your edits to the skill, checker, or docs. If you changed the rule itself,
   update both `skills/no-em-dashes/SKILL.md` and `AGENTS.md` together (see "Keeping the
   guidance in sync").
2. Run the checks below and make sure they pass.
3. Bump `"version"` in `.claude-plugin/plugin.json` (semantic versioning: patch for
   fixes, minor for additive changes, major for breaking ones).
4. Update `CHANGELOG.md`: add a section for the new version and move the relevant notes
   under it.
5. Commit and push to `main`.
6. If the catalog pins this skill to a `ref` or `sha` (rather than tracking the default
   branch), update that pin in `exmergo/exmergo-skills`. Otherwise users get the new
   version automatically on their next `marketplace update`.

## Pre-release checks

Run all three from the repo root before you push a release.

```bash
# 1. Plugin manifest is valid.
claude plugin validate .

# 2. The checker's unit tests pass (standard library only, no dependencies).
python -m unittest discover tests

# 3. Dogfood: the repo's own prose must be em-dash clean. This is the same command
#    CI runs: it scans every tracked .md/.mdc/.txt file and excludes the baseline
#    eval examples, which intentionally contain em dashes as evidence.
git ls-files '*.md' '*.mdc' '*.txt' \
  | grep -v '\.baseline\.txt$' \
  | xargs python skills/no-em-dashes/scripts/check_em_dashes.py
```

## Optional: submit to the Anthropic community marketplace

Once the repo is public, you can list the skill for wider discovery.

1. Run `claude plugin validate .` and make sure it passes.
2. Submit at `platform.claude.com/plugins/submit` (individual authors) or via the
   claude.ai directory admin form (Team/Enterprise orgs).
3. After it passes review, users install via
   `/plugin install no-em-dashes@claude-community`.
