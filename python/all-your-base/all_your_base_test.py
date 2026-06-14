# These tests are auto-generated with test data from:
# https://github.com/exercism/problem-specifications/tree/main/exercises/all-your-base/canonical-data.json
# File last updated on 2023-07-20

import unittest

import pytest
from all_your_base import (
    rebase,
)


class AllYourBaseTest(unittest.TestCase):
    def test_single_bit_one_to_decimal(self) -> None:
        assert rebase(2, [1], 10) == [1]

    def test_binary_to_single_decimal(self) -> None:
        assert rebase(2, [1, 0, 1], 10) == [5]

    def test_single_decimal_to_binary(self) -> None:
        assert rebase(10, [5], 2) == [1, 0, 1]

    def test_binary_to_multiple_decimal(self) -> None:
        assert rebase(2, [1, 0, 1, 0, 1, 0], 10) == [4, 2]

    def test_decimal_to_binary(self) -> None:
        assert rebase(10, [4, 2], 2) == [1, 0, 1, 0, 1, 0]

    def test_trinary_to_hexadecimal(self) -> None:
        assert rebase(3, [1, 1, 2, 0], 16) == [2, 10]

    def test_hexadecimal_to_trinary(self) -> None:
        assert rebase(16, [2, 10], 3) == [1, 1, 2, 0]

    def test_15_bit_integer(self) -> None:
        assert rebase(97, [3, 46, 60], 73) == [6, 10, 45]

    def test_empty_list(self) -> None:
        assert rebase(2, [], 10) == [0]

    def test_single_zero(self) -> None:
        assert rebase(10, [0], 2) == [0]

    def test_multiple_zeros(self) -> None:
        assert rebase(10, [0, 0, 0], 2) == [0]

    def test_leading_zeros(self) -> None:
        assert rebase(7, [0, 6, 0], 10) == [4, 2]

    def test_input_base_is_one(self) -> None:
        with pytest.raises(ValueError, match="input base must be >= 2") as err:
            rebase(1, [0], 10)
        assert isinstance(err.value, ValueError)
        assert err.value.args[0] == "input base must be >= 2"

    def test_input_base_is_zero(self) -> None:
        with pytest.raises(ValueError, match="input base must be >= 2") as err:
            rebase(0, [], 10)
        assert isinstance(err.value, ValueError)
        assert err.value.args[0] == "input base must be >= 2"

    def test_input_base_is_negative(self) -> None:
        with pytest.raises(ValueError, match="input base must be >= 2") as err:
            rebase(-2, [1], 10)
        assert isinstance(err.value, ValueError)
        assert err.value.args[0] == "input base must be >= 2"

    def test_negative_digit(self) -> None:
        with pytest.raises(ValueError, match="all digits must satisfy 0 <= d < input base") as err:
            rebase(2, [1, -1, 1, 0, 1, 0], 10)
        assert isinstance(err.value, ValueError)
        assert err.value.args[0] == "all digits must satisfy 0 <= d < input base"

    def test_invalid_positive_digit(self) -> None:
        with pytest.raises(ValueError, match="all digits must satisfy 0 <= d < input base") as err:
            rebase(2, [1, 2, 1, 0, 1, 0], 10)
        assert isinstance(err.value, ValueError)
        assert err.value.args[0] == "all digits must satisfy 0 <= d < input base"

    def test_output_base_is_one(self) -> None:
        with pytest.raises(ValueError, match="output base must be >= 2") as err:
            rebase(2, [1, 0, 1, 0, 1, 0], 1)
        assert isinstance(err.value, ValueError)
        assert err.value.args[0] == "output base must be >= 2"

    def test_output_base_is_zero(self) -> None:
        with pytest.raises(ValueError, match="output base must be >= 2") as err:
            rebase(10, [7], 0)
        assert isinstance(err.value, ValueError)
        assert err.value.args[0] == "output base must be >= 2"

    def test_output_base_is_negative(self) -> None:
        with pytest.raises(ValueError, match="output base must be >= 2") as err:
            rebase(2, [1], -7)
        assert isinstance(err.value, ValueError)
        assert err.value.args[0] == "output base must be >= 2"

    def test_both_bases_are_negative(self) -> None:
        with pytest.raises(ValueError, match="input base must be >= 2") as err:
            rebase(-2, [1], -7)
        assert isinstance(err.value, ValueError)
        assert err.value.args[0] == "input base must be >= 2"
