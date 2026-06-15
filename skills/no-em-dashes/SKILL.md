---
name: no-em-dashes
description: Enforce em-dash-free writing. Use this skill whenever you write or edit prose for the user, including drafts, emails, essays, reports, documentation, blog and social posts, marketing copy, creative writing, summaries, and rewrites, so the output contains zero em dashes and avoids the grammatical structures that invite them. Replace em-dash constructions with commas, semicolons, colons, periods, or parentheses, and recast sentences when a plain swap would read awkwardly. Trigger this even when the user does not explicitly mention em dashes, dashes, or punctuation, because the point is that every piece of writing comes out clean by default. Also apply it when polishing or proofreading text the user pastes in, and when the user asks for writing that does not look machine-generated.
---

# No Em Dashes

## What this does and why it matters

Guarantee that writing produced for the user contains no em dashes, and, just as important, that it is built out of sentences that never reach for one in the first place.

Two reasons this is worth real care:

1. Heavy em-dash use has become one of the most recognizable fingerprints of machine-written text. Many readers now read a dash-laden paragraph as "a bot wrote this." Clean punctuation keeps the writing reading as a person's.
2. The em dash quietly encourages a particular cadence: the dramatic pause, the tacked-on reveal, the breathless aside. Removing it forces tighter, more deliberate sentences, which is usually an improvement on its own.

The wrong way to satisfy this skill is to swap one em dash for a lookalike (a spaced hyphen, a double hyphen, a stray en dash). That is the same move wearing a disguise. The right way is to recognize the sentence shape that wanted the dash and rewrite so it is no longer needed.

## The rule

1. Never type an em dash in prose you write or edit. The character is U+2014. It does not appear in your output.
2. Do not smuggle the same pause back in. These are all banned when they do an em dash's job: a double hyphen (`word--word` or ` -- `), a hyphen padded with spaces (` - `), a stray en dash (U+2013) used between words, and the horizontal bar (U+2015). Replace the construction with real punctuation, not with another dash.
3. Reach for these instead, roughly in this order depending on the job: comma, semicolon, colon, period, parentheses (brackets).

### Do not overcorrect

The target is the em dash and its stand-ins acting as sentence punctuation. Nothing else.

- Keep ordinary hyphens in compounds: well-known, state-of-the-art, twenty-one, a five-year-old, mother-in-law.
- Keep hyphens and en dashes in genuine number, date, and score ranges if they appear (for example 10-20, 2019-2024, a 3-1 win), and keep hyphens in code, file paths, URLs, command flags, and math. Never "fix" a minus sign.
- Leave Markdown structure alone. A line of three or more hyphens (a front matter delimiter or a horizontal rule) and a table separator row like `| --- | --- |` are formatting, not punctuation. A run of three hyphens used as a pause inside a sentence is still a stand-in, so recast that.
- Do not become so dash-averse that you start chopping sentences into choppy fragments. Good prose still flows; you are removing a crutch, not the connective tissue.

## Refuse the sentence shape, not just the character

An em dash is almost always doing one of a small number of rhetorical jobs. Identify the job, then use the matching replacement. If you only swap the character you sometimes create a comma splice or a limp sentence, so when in doubt, recast.

### 1. The dramatic reveal or tacked-on punchline

The construction reached for most often. Some setup, then a dash, then a payoff.

- Avoid: She wanted one thing [em dash] to win.
- Prefer (colon, when the payoff explains the setup): She wanted one thing: to win.
- Prefer (two sentences, for punch): She wanted one thing. To win.

### 2. The "not just X, but Y" pivot

- Avoid: This isn't a tool [em dash] it's a platform.
- Prefer (recast, usually the cleanest): This is a platform, not just a tool.
- Prefer (semicolon): This isn't a tool; it's a platform.
- Prefer (two sentences): This is more than a tool. It's a platform.

### 3. The interruptive aside (parenthetical)

- Avoid: The plan [em dash] which nobody liked [em dash] was scrapped.
- Prefer (commas, for a mild aside): The plan, which nobody liked, was scrapped.
- Prefer (parentheses, for a true aside): The plan (which nobody liked) was scrapped.

### 4. Two related independent clauses joined for effect

- Avoid: It compiles [em dash] and it's fast.
- Prefer (semicolon, for a tight link): It compiles; it's fast.
- Prefer (comma plus conjunction): It compiles, and it's fast.
- Prefer (period): It compiles. It is also fast.

### 5. The summary dash (gathering a list into a conclusion)

- Avoid: Speed, clarity, polish [em dash] that's the whole goal.
- Prefer (recast around a colon): The whole goal is speed, clarity, and polish.
- Prefer (period): Speed, clarity, polish. That is the whole goal.

### 6. An abrupt break or interruption in dialogue

This is the one job with no clean comma or semicolon swap, so handle it honestly rather than forcing a bad substitute.

- Lean on the surrounding narration to carry the beat, and choose punctuation by whether the line trails off or is cut clean.
- Avoid: "But I never said[em dash]" she started.
- Prefer (a hard stop): "But I never said." She caught herself.
- Prefer (trailing off, using an ellipsis): "But I never said..."

## Quoting existing text

If you are quoting a source word for word and the original contains an em dash, you may keep it inside the direct quotation, because silently altering a quote misrepresents the source. Prefer to paraphrase so the question does not arise. Never introduce an em dash in your own voice, and never add one to a quote that did not have it.

## A quick self-check before you finish

Scan the finished text for the em dash and its stand-ins, then fix any that punctuate a sentence.

If code execution is available, run the bundled checker on a draft file or via stdin:

```bash
python "${CLAUDE_SKILL_DIR}/scripts/check_em_dashes.py" path/to/draft.txt
echo "Your text here" | python "${CLAUDE_SKILL_DIR}/scripts/check_em_dashes.py"
```

`${CLAUDE_SKILL_DIR}` resolves to this skill's folder however it was installed (personal, project, or plugin). If it is not set, point at `scripts/check_em_dashes.py` inside this skill directory. It prints every hit with its location and a suggested fix, and exits nonzero if anything is found. If you cannot run code, do the scan by eye: search the text for the em dash character, for a double hyphen, and for a hyphen with a space on each side, and rewrite each one using the playbook above.

## Worked examples

In each "Before" line below, `[em dash]` marks where the original used the em dash character. The "After" line shows the clean rewrite.

**Example 1 (reveal):**
Before: The data was clear [em dash] engagement had collapsed.
After: The data was clear: engagement had collapsed.

**Example 2 (pivot):**
Before: We don't sell software [em dash] we sell outcomes.
After: We sell outcomes, not software.

**Example 3 (aside):**
Before: Our flagship store [em dash] the one downtown [em dash] closes in May.
After: Our flagship store (the one downtown) closes in May.

**Example 4 (two clauses):**
Before: The fix shipped on Friday [em dash] nobody noticed until Monday.
After: The fix shipped on Friday; nobody noticed until Monday.

**Example 5 (summary):**
Before: Lower cost, faster turnaround, fewer defects [em dash] that's the pitch.
After: The pitch is lower cost, faster turnaround, and fewer defects.
