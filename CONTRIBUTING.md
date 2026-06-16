# Contributing

Thanks for your interest in improving `no-em-dashes`. Contributions of all sizes are
welcome, from a typo fix to a new entry in the rewrite playbook.

## Ways to help

- **Improve the skill instructions.** If you find a sentence shape the skill handles
  badly, or a rewrite that reads awkwardly, propose a clearer rule or a better worked
  example. The guidance is mirrored in two self-contained files, `skills/no-em-dashes/SKILL.md`
  (Claude Code) and `AGENTS.md` (all other agents), so a change to the rule itself
  belongs in both. See "Keeping the guidance in sync" in
  [MAINTAINING.md](MAINTAINING.md) for why.
- **Sharpen the checker.** If `skills/no-em-dashes/scripts/check_em_dashes.py` flags
  something legitimate (a false positive) or misses a real stand-in (a false
  negative), open an issue with the exact text, or send a fix with a test that covers
  it.
- **Add evaluation prompts.** Realistic writing tasks that tempt a model into em
  dashes are valuable. The current set lives in
  `skills/no-em-dashes/evals/evals.json`.

## Before you open a pull request

1. **Run the tests.** They use only the standard library:

   ```bash
   python -m unittest discover tests
   ```

   If you change the checker's behavior, add or update a test so the new behavior is
   pinned down.

2. **Keep your own writing clean.** This is a project about em-dash-free prose, so the
   prose in the docs, your commit messages, and your pull request description should
   practice what we preach. The checker can tell you if you slipped:

   ```bash
   python skills/no-em-dashes/scripts/check_em_dashes.py path/to/your/file.md
   ```

3. **Keep the two guidance files in sync.** If your change touches the rule itself,
   update both `skills/no-em-dashes/SKILL.md` and `AGENTS.md` in the same pull request.
   The per-tool files under `.cursor/`, `.github/`, and `.windsurf/` point to `AGENTS.md`
   and do not need changing.

4. **Explain the why.** For changes to the skill, a sentence on the reasoning helps
   more than the change alone. The skill works best when the model understands the
   intent, not just the rule.

## Reporting issues

Open a GitHub issue with a clear title, the input text involved, what you expected,
and what actually happened. For checker bugs, the smallest snippet that reproduces the
problem is ideal.

## Code of conduct

By participating you agree to uphold our [Code of Conduct](CODE_OF_CONDUCT.md).
