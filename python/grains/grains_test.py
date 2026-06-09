# These tests are auto-generated with test data from:
# https://github.com/exercism/problem-specifications/tree/main/exercises/grains/canonical-data.json
# File last updated on 2026-02-19

import unittest

import pytest

from grains import (
    MAX_SQUARE,
    MIN_SQUARE,
    square,
    total,
)


class GrainsTest(unittest.TestCase):

    def test_grains_on_square_1(self) -> None:
        assert square(1) == 1

    def test_grains_on_square_2(self) -> None:
        assert square(2) == 2

    def test_grains_on_square_3(self) -> None:
        assert square(3) == 4

    def test_grains_on_square_4(self) -> None:
        assert square(4) == 8

    def test_grains_on_square_16(self) -> None:
        assert square(16) == 32768

    def test_grains_on_square_32(self) -> None:
        assert square(32) == 2147483648

    def test_grains_on_square_64(self) -> None:
        assert square(64) == 9223372036854775808

    def test_square_0_is_invalid(self) -> None:
        with pytest.raises(ValueError,
                           match=f"square must be between {MIN_SQUARE} and {MAX_SQUARE}") as err:
            square(0)
        assert isinstance(err.value, ValueError)
        assert err.value.args[0] == "square must be between 1 and 64"

    def test_negative_square_is_invalid(self) -> None:
        with pytest.raises(ValueError,
                           match=f"square must be between {MIN_SQUARE} and {MAX_SQUARE}") as err:
            square(-1)
        assert isinstance(err.value, ValueError)
        assert err.value.args[0] == f"square must be between {MIN_SQUARE} and {MAX_SQUARE}"

    def test_square_greater_than_64_is_invalid(self) -> None:
        with pytest.raises(ValueError,
                           match=f"square must be between {MIN_SQUARE} and {MAX_SQUARE}") as err:
            square(65)
        assert isinstance(err.value, ValueError)
        assert err.value.args[0] == "square must be between 1 and 64"

    def test_returns_the_total_number_of_grains_on_the_board(self) -> None:
        assert total() == 18446744073709551615
