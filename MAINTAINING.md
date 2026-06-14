# Maintaining and releasing

This repo is both a Claude Code plugin (`no-em-dashes`) and its own marketplace
(`exmergo-skills`). The marketplace is "live" whenever `.claude-plugin/marketplace.json`
exists at the root of a git repo your users can reach. There is no separate publish or
registration step with Anthropic for a self-hosted marketplace.

## Repository layout

```
.claude-plugin/
  plugin.json          plugin manifest: name, version, author, repository
  marketplace.json     marketplace catalog; lists this plugin with "source": "./"
skills/
  no-em-dashes/        the skill (SKILL.md, scripts/, evals/)
tests/                 standard-library unit tests for the checker
```

The plugin's `source` is `"./"`, meaning the plugin lives at the repo root. This works
for GitHub and other git-based marketplace adds.

## First-time publish

1. Create the repo at `github.com/exmergo/skill-no-em-dashes`.
2. Push this code to the `main` branch (marketplace adds read the default branch):

   ```bash
   git add -A
   git commit -m "Release no-em-dashes <version>"
   git remote add origin git@github.com:exmergo/skill-no-em-dashes.git
   git push -u origin main
   ```

That is the publish. With `marketplace.json` at the root, the marketplace is reachable.

## How users install

```
/plugin marketplace add exmergo/skill-no-em-dashes
/plugin install no-em-dashes@exmergo-skills
```

To pull later changes, a user runs `/plugin marketplace update exmergo-skills`.

## Private first, public later

You can ship privately to the team, then open it up with no repackaging.

- **While private:** the repo works as a marketplace, but each teammate needs read
  access to it plus working git auth on their machine (SSH keys or `gh auth login`).
  Rule of thumb: if their `git clone git@github.com:exmergo/skill-no-em-dashes.git`
  works in a terminal, the `/plugin marketplace add` will work too.
- **Going public:** change the repo visibility in GitHub settings. Nothing in the repo
  changes, existing installs keep working, and the `exmergo/skill-no-em-dashes` add
  command then works for anyone with no auth.
- **Before going public:** scrub the git history for secrets, since public exposes
  every past commit, not just the current files.

## Cutting a release (any change after the first publish)

Updates are version-gated: because `plugin.json` sets a `version`, users only receive
changes when you bump it. Do not also set `version` in `marketplace.json`; if both are
set, the `plugin.json` value silently wins.

1. Make your edits to the skill, checker, or docs.
2. Run the checks below and make sure they pass.
3. Bump `"version"` in `.claude-plugin/plugin.json` (semantic versioning: patch for
   fixes, minor for additive changes, major for breaking ones).
4. Commit and push to `main`.
5. Users pick it up with `/plugin marketplace update exmergo-skills`.

## Pre-release checks

Run all three from the repo root before you push a release.

```bash
# 1. Manifests are valid (also confirms the plugin source resolves).
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

Once the repo is public, you can list it for wider discovery.

1. Run `claude plugin validate .` and make sure it passes.
2. Submit at `platform.claude.com/plugins/submit` (individual authors) or via the
   claude.ai directory admin form (Team/Enterprise orgs).
3. After it passes review, users install via
   `/plugin install no-em-dashes@claude-community`.

## A note on the marketplace name

A marketplace name is global per user (a second marketplace with the same name
replaces the first). This repo names its marketplace `exmergo-skills`. If Exmergo later
wants a single catalog spanning several skills, the cleaner pattern is a dedicated
`exmergo/exmergo-skills` repo whose `marketplace.json` references each plugin repo
(this one included) via a `github` source, rather than each skill repo also calling
itself `exmergo-skills`.
