# These tests are auto-generated with test data from:
# https://github.com/exercism/problem-specifications/tree/main/exercises/matching-brackets/canonical-data.json
# File last updated on 2023-07-19

import unittest

from matching_brackets import (
    is_paired,
)


class MatchingBracketsTest(unittest.TestCase):
    def test_paired_square_brackets(self) -> None:
        assert is_paired("[]")

    def test_empty_string(self) -> None:
        assert is_paired("")

    def test_unpaired_brackets(self) -> None:
        assert not is_paired("[[")

    def test_wrong_ordered_brackets(self) -> None:
        assert not is_paired("}{")

    def test_wrong_closing_bracket(self) -> None:
        assert not is_paired("{]")

    def test_paired_with_whitespace(self) -> None:
        assert is_paired("{ }")

    def test_partially_paired_brackets(self) -> None:
        assert not is_paired("{[])")

    def test_simple_nested_brackets(self) -> None:
        assert is_paired("{[]}")

    def test_several_paired_brackets(self) -> None:
        assert is_paired("{}[]")

    def test_paired_and_nested_brackets(self) -> None:
        assert is_paired("([{}({}[])])")

    def test_unopened_closing_brackets(self) -> None:
        assert not is_paired("{[)][]}")

    def test_unpaired_and_nested_brackets(self) -> None:
        assert not is_paired("([{])")

    def test_paired_and_wrong_nested_brackets(self) -> None:
        assert not is_paired("[({]})")

    def test_paired_and_wrong_nested_brackets_but_innermost_are_correct(self) -> None:
        assert not is_paired("[({}])")

    def test_paired_and_incomplete_brackets(self) -> None:
        assert not is_paired("{}[")

    def test_too_many_closing_brackets(self) -> None:
        assert not is_paired("[]]")

    def test_early_unexpected_brackets(self) -> None:
        assert not is_paired(")()")

    def test_early_mismatched_brackets(self) -> None:
        assert not is_paired("{)()")

    def test_math_expression(self) -> None:
        assert is_paired("(((185 + 223.85) * 15) - 543)/2")

    def test_complex_latex_expression(self) -> None:
        assert is_paired(
            "\\left(\\begin{array}{cc} \\frac{1}{3} & x\\\\ "
            "\\mathrm{e}^{x} &... x^2 \\end{array}\\right)")
