# These tests are auto-generated with test data from:
# https://github.com/exercism/problem-specifications/tree/main/exercises/collatz-conjecture/canonical-data.json
# File last updated on 2023-07-20

import unittest

import pytest
from collatz_conjecture import (
    steps,
)


class CollatzConjectureTest(unittest.TestCase):
    def test_zero_steps_for_one(self) -> None:
        assert steps(1) == 0

    def test_divide_if_even(self) -> None:
        assert steps(16) == 4

    def test_even_and_odd_steps(self) -> None:
        assert steps(12) == 9

    def test_large_number_of_even_and_odd_steps(self) -> None:
        assert steps(1000000) == 152

    def test_zero_is_an_error(self) -> None:
        with pytest.raises(ValueError, match="Only positive integers are allowed") as err:
            steps(0)
        assert isinstance(err.value, ValueError)
        assert err.value.args[0] == "Only positive integers are allowed"

    def test_negative_value_is_an_error(self) -> None:
        with pytest.raises(ValueError, match="Only positive integers are allowed") as err:
            steps(-15)
        assert isinstance(err.value, ValueError)
        assert err.value.args[0] == "Only positive integers are allowed"
