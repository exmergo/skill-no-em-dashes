# Writing style: no em dashes

These rules apply to any prose you write or edit: drafts, documentation, commit
messages, pull request descriptions, comments, emails, marketing copy, and essays. The
goal is writing that contains no em dashes and is built from sentences that never reach
for one in the first place.

Why it matters: heavy em-dash use is one of the most recognizable fingerprints of
machine-written text, and removing it forces tighter, more deliberate sentences.

## The rule

1. Never use an em dash (the character U+2014) as punctuation.
2. Do not smuggle the same pause back in with a look-alike. These are banned when they
   do an em dash's job: a double hyphen (`word--word` or a spaced ` -- `), a hyphen
   padded with spaces (` - `), a stray en dash (U+2013) between words, and the
   horizontal bar (U+2015).
3. Replace the construction with real punctuation, roughly in this order: comma,
   semicolon, colon, period, parentheses. When a plain swap reads awkwardly, recast the
   sentence rather than forcing a substitute.

## Match the replacement to the job

An em dash is almost always doing one of a few jobs. Identify it, then replace it.
In the examples below, `[em dash]` marks where the original reached for one.

- Dramatic reveal ("She wanted one thing [em dash] to win"): use a colon, or split
  into two sentences.
- "Not X but Y" pivot ("This isn't a tool [em dash] it's a platform"): recast as "This
  is a platform, not just a tool", or use a semicolon.
- Interruptive aside ("The plan [em dash] which nobody liked [em dash] was scrapped"):
  use commas for a mild aside, parentheses for a true one.
- Two joined clauses ("It compiles [em dash] and it's fast"): use a semicolon, a comma
  plus conjunction, or two sentences.
- Summary dash ("Speed, clarity, polish [em dash] that's the goal"): recast around a
  colon, or split into sentences.
- Interrupted dialogue: use a hard stop carried by narration, or an ellipsis for a line
  that trails off. This is the one job with no clean comma or semicolon swap.

## Do not overcorrect

Only dashes acting as sentence punctuation are the target. Leave these alone:

- Hyphenated compounds: well-known, state-of-the-art, twenty-one, mother-in-law.
- Number, date, and score ranges (10-20, 2019-2024, a 3-1 win), and hyphens in code,
  file paths, URLs, command flags, and math. Never "fix" a minus sign.
- Markdown structure: a line of three or more hyphens (front matter delimiters and
  horizontal rules) and table separator rows like `| --- | --- |`.
- Do not chop prose into choppy fragments. Good writing still flows; you are removing a
  crutch, not the connective tissue.

## Optional checker

If this repository ships the checker and you can run a shell command, scan a draft
before finishing:

```bash
python skills/no-em-dashes/scripts/check_em_dashes.py path/to/draft.txt
```

It prints every em dash or stand-in used as punctuation, with a suggested fix, and
exits nonzero if anything is found.
