# Evaluation results

These are the results from the first evaluation pass of the skill. The setup was
simple: run three realistic writing prompts twice, once with the skill loaded and
once without it (a plain model baseline), then check every output for em dashes and
their stand-ins.

The prompts live in [`../evals.json`](../evals.json):

1. A punchy product launch announcement (marketing copy).
2. A warm release-delay email to a team (explanatory prose).
3. A break-room argument where one speaker keeps getting cut off (dialogue with interruptions).

## Headline numbers

See [`benchmark.md`](benchmark.md) for the full table. The short version:

| Configuration | Outputs free of em dashes |
|---------------|---------------------------|
| With the skill | 3 of 3 |
| Baseline (no skill) | 1 of 3 |

The baseline reached for em dashes in two of the three prompts: three of them in the
email, five in the dialogue. The launch announcement came out clean either way, which
tells us short marketing copy is less of a temptation than reflective prose or dialogue.

## Why the dialogue case matters most

Interrupted dialogue is the one job an em dash does that has no clean comma or
semicolon swap, so it is the hardest test. The [`examples/`](examples) folder has the
two discriminating prompts side by side:

- `breakroom-dialogue.baseline.txt` cuts speakers off with em dashes (`before the—`).
- `breakroom-dialogue.with-skill.txt` cuts them off mid-clause and lets the narration
  carry the beat (`if you'd looped me in before sending the deck to.`), which reads as
  a real interruption without the dash.

The same contrast shows up in the email examples, where the baseline uses dashes for
asides and the skill version uses commas, parentheses, and separate sentences.

## A caveat on cost

Loading the skill and running the checker adds time and tokens (see the benchmark).
That is the price of the self-check. For a one-shot writing task it is well worth it;
for very light edits you can skip the checker and just apply the playbook by eye.

## Reproducing

The prompts are in `evals.json`. Run each one through your model twice (with and
without the skill in context), then check the outputs:

```bash
python ../../scripts/check_em_dashes.py path/to/output.txt
```
