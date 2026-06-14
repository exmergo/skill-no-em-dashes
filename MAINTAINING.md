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
tests/                 standard-library unit tests for the checker
```

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

1. Make your edits to the skill, checker, or docs.
2. Run the checks below and make sure they pass.
3. Bump `"version"` in `.claude-plugin/plugin.json` (semantic versioning: patch for
   fixes, minor for additive changes, major for breaking ones).
4. Commit and push to `main`.
5. If the catalog pins this skill to a `ref` or `sha` (rather than tracking the default
   branch), update that pin in `exmergo/exmergo-skills`. Otherwise users get the new
   version automatically on their next `marketplace update`.

## Pre-release checks

Run all three from the repo root before you push a release.

```bash
# 1. Plugin manifest is valid.
claude plugin validate .

# 2. The checker's unit tests pass (standard library only, no dependencies).
python -m unittest discover tests

# 3. Dogfood: the repo's own prose must be em-dash clean. The baseline example
#    files under evals/results/examples/ are evidence and intentionally contain
#    em dashes, so exclude them.
for f in README.md CONTRIBUTING.md CODE_OF_CONDUCT.md MAINTAINING.md \
         skills/no-em-dashes/SKILL.md \
         skills/no-em-dashes/evals/results/README.md \
         skills/no-em-dashes/evals/results/benchmark.md \
         skills/no-em-dashes/evals/results/examples/*.with-skill.txt; do
  python skills/no-em-dashes/scripts/check_em_dashes.py "$f"
done
```

## Optional: submit to the Anthropic community marketplace

Once the repo is public, you can list the skill for wider discovery.

1. Run `claude plugin validate .` and make sure it passes.
2. Submit at `platform.claude.com/plugins/submit` (individual authors) or via the
   claude.ai directory admin form (Team/Enterprise orgs).
3. After it passes review, users install via
   `/plugin install no-em-dashes@claude-community`.
