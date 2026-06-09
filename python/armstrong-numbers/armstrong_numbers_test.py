# These tests are auto-generated with test data from:
# https://github.com/exercism/problem-specifications/tree/main/exercises/armstrong-numbers/canonical-data.json
# File last updated on 2023-07-20

import unittest

from armstrong_numbers import (
    is_armstrong_number,
)


class ArmstrongNumbersTest(unittest.TestCase):
    def test_zero_is_an_armstrong_number(self) -> None:
        assert is_armstrong_number(0) is True

    def test_single_digit_numbers_are_armstrong_numbers(self) -> None:
        assert is_armstrong_number(5) is True

    def test_there_are_no_two_digit_armstrong_numbers(self) -> None:
        assert is_armstrong_number(10) is False

    def test_three_digit_number_that_is_an_armstrong_number(self) -> None:
        assert is_armstrong_number(153) is True

    def test_three_digit_number_that_is_not_an_armstrong_number(self) -> None:
        assert is_armstrong_number(100) is False

    def test_four_digit_number_that_is_an_armstrong_number(self) -> None:
        assert is_armstrong_number(9474) is True

    def test_four_digit_number_that_is_not_an_armstrong_number(self) -> None:
        assert is_armstrong_number(9475) is False

    def test_seven_digit_number_that_is_an_armstrong_number(self) -> None:
        assert is_armstrong_number(9926315) is True

    def test_seven_digit_number_that_is_not_an_armstrong_number(self) -> None:
        assert is_armstrong_number(9926314) is False
