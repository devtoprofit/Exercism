# These tests are auto-generated with test data from:
# https://github.com/exercism/problem-specifications/tree/main/exercises/perfect-numbers/canonical-data.json
# File last updated on 2026-02-25

import unittest

import pytest
from perfect_numbers import (
    classify,
)


class PerfectNumbersTest(unittest.TestCase):
    def test_smallest_perfect_number_is_classified_correctly(self) -> None:
        assert classify(6) == "perfect"

    def test_medium_perfect_number_is_classified_correctly(self) -> None:
        assert classify(28) == "perfect"

    def test_large_perfect_number_is_classified_correctly(self) -> None:
        assert classify(33550336) == "perfect"


class AbundantNumbersTest(unittest.TestCase):
    def test_smallest_abundant_number_is_classified_correctly(self) -> None:
        assert classify(12) == "abundant"

    def test_medium_abundant_number_is_classified_correctly(self) -> None:
        assert classify(30) == "abundant"

    def test_large_abundant_number_is_classified_correctly(self) -> None:
        assert classify(33550335) == "abundant"

    def test_perfect_square_abundant_number_is_classified_correctly(self) -> None:
        assert classify(196) == "abundant"


class DeficientNumbersTest(unittest.TestCase):
    def test_smallest_prime_deficient_number_is_classified_correctly(self) -> None:
        assert classify(2) == "deficient"

    def test_smallest_non_prime_deficient_number_is_classified_correctly(self) -> None:
        assert classify(4) == "deficient"

    def test_medium_deficient_number_is_classified_correctly(self) -> None:
        assert classify(32) == "deficient"

    def test_large_deficient_number_is_classified_correctly(self) -> None:
        assert classify(33550337) == "deficient"

    def test_edge_case_no_factors_other_than_itself_is_classified_correctly(self) -> None:
        assert classify(1) == "deficient"


class InvalidInputsTest(unittest.TestCase):
    def test_zero_is_rejected_as_it_is_not_a_positive_integer(self) -> None:
        with pytest.raises(ValueError,
                           match="Classification is only possible for positive integers") as err:
            classify(0)
        assert type(err.value) == ValueError  # noqa: E721
        assert err.value.args[0] == "Classification is only possible for positive integers."

    def test_negative_integer_is_rejected_as_it_is_not_a_positive_integer(self) -> None:
        with pytest.raises(ValueError,
                           match="Classification is only possible for positive integers") as err:
            classify(-1)
        assert type(err.value) == ValueError  # noqa: E721
        assert err.value.args[0] == "Classification is only possible for positive integers."
