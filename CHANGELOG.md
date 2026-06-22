# Changelog

All notable changes to this project are documented here. The format is based on
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to
[Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.1] - 2026-06-22

### Changed

- The catalog marketplace was renamed from `exmergo-skills` to `exmergo`, and its GitHub
  repo was renamed from `exmergo/exmergo-skills` to `exmergo/exmergo-agent-plugins`. Installs
  and updates now use `no-em-dashes@exmergo` and `marketplace update exmergo`, and the catalog
  is added with `marketplace add exmergo/exmergo-agent-plugins` (GitHub redirects the old path).
  Anyone who added it under the old name re-registers once with
  `/plugin marketplace remove exmergo-skills` then `/plugin marketplace add exmergo/exmergo-agent-plugins`.

## [1.1.0] - 2026-06-16

### Added

- Cross-agent distribution. `AGENTS.md` is the canonical guidance, read automatically
  by Cursor, GitHub Copilot agent mode, Codex, Continue, Aider, Windsurf, and others.
  Thin per-tool pointer rules sit alongside it: `.cursor/rules/no-em-dashes.mdc`,
  `.github/copilot-instructions.md`, and `.windsurf/rules/no-em-dashes.md`.
- Two long-form evals (a 1000-word essay and a 1000-word landing page) and
  `skills/no-em-dashes/evals/results/em_dash_counts.csv`, recording em dash counts per
  eval with the skill versus without it.
- A hero image in the README.
- Guidance-sync documentation in `MAINTAINING.md` and `CONTRIBUTING.md`, explaining why
  `SKILL.md` and `AGENTS.md` mirror the same rule and how to keep them aligned.
- This `CHANGELOG.md` and a GitHub Actions CI workflow (unit tests across Python 3.9,
  3.11, and 3.13, plus an em-dash dogfood check over the repo's own prose).

## [1.0.1] - 2026-06-15

### Fixed

- The checker no longer flags runs of three or more hyphens used as Markdown structure
  (front matter delimiters, horizontal rules, and table separator rows like
  `| --- | --- |`). A run of three hyphens used as a pause inside a sentence is still
  flagged.

### Added

- Regression tests covering Markdown structure (front matter, horizontal rules, table
  separators) and confirming that prose stand-ins still flag.

## [1.0.0] - 2026-06-15

### Added

- Initial release: the `no-em-dashes` skill (`SKILL.md`) with a rewrite playbook for
  each rhetorical job an em dash does.
- A dependency-free checker (`skills/no-em-dashes/scripts/check_em_dashes.py`) that
  flags em dashes and their stand-ins while leaving legitimate hyphens, ranges, code,
  and URLs alone, with a standard-library unit test suite.
- Evaluation prompts and recorded first-pass results.
- Packaging as a Claude Code plugin, distributed through the `exmergo-skills`
  marketplace, with an MIT license, a contributing guide, and a code of conduct.

[1.1.1]: https://github.com/exmergo/skill-no-em-dashes/releases/tag/v1.1.1
[1.1.0]: https://github.com/exmergo/skill-no-em-dashes/releases/tag/v1.1.0
[1.0.1]: https://github.com/exmergo/skill-no-em-dashes/releases/tag/v1.0.1
[1.0.0]: https://github.com/exmergo/skill-no-em-dashes/releases/tag/v1.0.0
