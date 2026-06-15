"""Tests for the em-dash checker.

Run from the repository root with:

    python -m unittest discover tests

No third-party dependencies; this uses only the standard library so it runs
anywhere Python 3 does.
"""

import importlib.util
import os
import unittest

# Load the checker module directly from the skill's scripts directory, since it
# is a standalone script rather than an installed package.
_HERE = os.path.dirname(os.path.abspath(__file__))
_CHECKER_PATH = os.path.join(
    _HERE, "..", "skills", "no-em-dashes", "scripts", "check_em_dashes.py"
)
_spec = importlib.util.spec_from_file_location("check_em_dashes", _CHECKER_PATH)
checker = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(checker)


def hit_count(text):
    """Number of dash problems the checker finds in a string."""
    return len(checker.check(text))


class FlagsRealProblems(unittest.TestCase):
    """Constructions that do an em dash's job must be caught."""

    def test_em_dash(self):
        self.assertEqual(hit_count("She wanted one thing — to win."), 1)

    def test_horizontal_bar(self):
        self.assertEqual(hit_count("Speed, clarity ― that is the goal."), 1)

    def test_double_hyphen_between_words(self):
        self.assertEqual(hit_count("This isn't a tool--it's a platform."), 1)

    def test_double_hyphen_spaced(self):
        self.assertEqual(hit_count("It compiles -- and it's fast."), 1)

    def test_spaced_hyphen_between_words(self):
        self.assertEqual(hit_count("The plan - which nobody liked - was scrapped."), 2)

    def test_en_dash_between_words(self):
        self.assertEqual(hit_count("It compiles – and it is fast."), 1)

    def test_multiple_on_one_line(self):
        self.assertEqual(hit_count("Yes — no — maybe."), 2)


class LeavesLegitimateUsesAlone(unittest.TestCase):
    """The checker targets sentence punctuation, not every hyphen."""

    def test_compound_words(self):
        text = "A well-known, state-of-the-art tool for a five-year-old."
        self.assertEqual(hit_count(text), 0)

    def test_compound_with_mother_in_law(self):
        self.assertEqual(hit_count("My mother-in-law is twenty-one."), 0)

    def test_number_ranges(self):
        self.assertEqual(hit_count("Pages 10-20, years 2019-2024, a 3-1 win."), 0)

    def test_en_dash_number_range(self):
        self.assertEqual(hit_count("The years 2019–2024 were busy."), 0)

    def test_minus_sign_in_math(self):
        self.assertEqual(hit_count("The result of 5 - 3 = 2 is positive."), 0)

    def test_command_flag(self):
        self.assertEqual(hit_count("Run `npm install --verbose` now."), 0)

    def test_url_with_hyphens(self):
        self.assertEqual(hit_count("See https://example.com/a-b-c for details."), 0)

    def test_file_path(self):
        self.assertEqual(hit_count("Open src/some-module/index-file.js to start."), 0)

    def test_list_marker(self):
        self.assertEqual(hit_count("- first item\n- second item"), 0)

    def test_inline_code_with_double_hyphen(self):
        self.assertEqual(hit_count("Pass the `--dry-run` flag to preview."), 0)

    def test_fenced_code_block_is_skipped(self):
        text = "Here is code:\n```\ngit log --oneline\nfoo -- bar\n```\nDone."
        self.assertEqual(hit_count(text), 0)


class MarkdownStructureIsNotFlagged(unittest.TestCase):
    """Runs of hyphens used as markdown formatting are not em-dash stand-ins."""

    def test_front_matter_delimiter(self):
        text = "---\ntitle: Hello\n---\nBody text here."
        self.assertEqual(hit_count(text), 0)

    def test_horizontal_rule(self):
        self.assertEqual(hit_count("Above.\n\n---\n\nBelow."), 0)

    def test_longer_horizontal_rule(self):
        self.assertEqual(hit_count("Above.\n\n----\n\nBelow."), 0)

    def test_table_separator_spaced(self):
        self.assertEqual(hit_count("| Col A | Col B |\n| --- | --- |\n| 1 | 2 |"), 0)

    def test_table_separator_unspaced(self):
        self.assertEqual(hit_count("| A | B |\n|---|---|\n| 1 | 2 |"), 0)

    def test_table_separator_with_alignment_colons(self):
        self.assertEqual(hit_count("| A | B |\n| :-- | --: |\n| 1 | 2 |"), 0)

    def test_prose_triple_hyphen_still_flagged(self):
        # A run of three hyphens used as a pause in prose is still a stand-in.
        self.assertEqual(hit_count("She paused --- then left."), 1)

    def test_double_hyphen_in_prose_still_flagged(self):
        # The fix must not weaken the ordinary double-hyphen case.
        self.assertEqual(hit_count("This isn't a tool -- it's a platform."), 1)


class ReportsLocationAndExitCode(unittest.TestCase):
    """Hits carry a 1-indexed line and column; clean text reports nothing."""

    def test_line_and_column_are_one_indexed(self):
        # Em dash sits at column 5 on line 2 (1-indexed).
        hits = checker.check("clean line\nbad — here")
        self.assertEqual(len(hits), 1)
        line_no, col_no, matched, _fix = hits[0]
        self.assertEqual(line_no, 2)
        self.assertEqual(col_no, 5)
        self.assertEqual(matched, "—")

    def test_clean_text_has_no_hits(self):
        self.assertEqual(hit_count("A perfectly clean sentence, with commas."), 0)


if __name__ == "__main__":
    unittest.main()
