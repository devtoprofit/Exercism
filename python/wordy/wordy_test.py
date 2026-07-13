# These tests are auto-generated with test data from:
# https://github.com/exercism/problem-specifications/tree/main/exercises/wordy/canonical-data.json
# File last updated on 2026-05-22

import unittest

import pytest

from wordy import (
    answer,
)


class WordyTest(unittest.TestCase):
    def test_just_a_number(self) -> None:
        assert answer("What is 5?") == 5

    def test_just_a_zero(self) -> None:
        assert answer("What is 0?") == 0

    def test_just_a_negative_number(self) -> None:
        assert answer("What is -123?") == -123

    def test_addition(self) -> None:
        assert answer("What is 1 plus 1?") == 2

    def test_addition_with_a_left_hand_zero(self) -> None:
        assert answer("What is 0 plus 2?") == 2

    def test_addition_with_a_right_hand_zero(self) -> None:
        assert answer("What is 3 plus 0?") == 3

    def test_more_addition(self) -> None:
        assert answer("What is 53 plus 2?") == 55

    def test_addition_with_negative_numbers(self) -> None:
        assert answer("What is -1 plus -10?") == -11

    def test_large_addition(self) -> None:
        assert answer("What is 123 plus 45678?") == 45801

    def test_subtraction(self) -> None:
        assert answer("What is 4 minus -12?") == 16

    def test_multiplication(self) -> None:
        assert answer("What is -3 multiplied by 25?") == -75

    def test_division(self) -> None:
        assert answer("What is 33 divided by -3?") == -11

    def test_multiple_additions(self) -> None:
        assert answer("What is 1 plus 1 plus 1?") == 3

    def test_addition_and_subtraction(self) -> None:
        assert answer("What is 1 plus 5 minus -2?") == 8

    def test_multiple_subtraction(self) -> None:
        assert answer("What is 20 minus 4 minus 13?") == 3

    def test_subtraction_then_addition(self) -> None:
        assert answer("What is 17 minus 6 plus 3?") == 14

    def test_multiple_multiplication(self) -> None:
        assert answer("What is 2 multiplied by -2 multiplied by 3?") == -12

    def test_addition_and_multiplication(self) -> None:
        assert answer("What is -3 plus 7 multiplied by -2?") == -8

    def test_multiple_division(self) -> None:
        assert answer("What is -12 divided by 2 divided by -3?") == 2

    def test_unknown_operation(self) -> None:
        with pytest.raises(ValueError, match="unknown operation") as err:
            answer("What is 52 cubed?")
        assert isinstance(err.value, ValueError)
        assert err.value.args[0] == "unknown operation"

    def test_reject_problem_missing_an_operand(self) -> None:
        with pytest.raises(ValueError, match="syntax error") as err:
            answer("What is 1 plus?")
        assert isinstance(err.value, ValueError)
        assert err.value.args[0] == "syntax error"

    def test_reject_problem_with_no_operands_or_operators(self) -> None:
        with pytest.raises(ValueError, match="syntax error") as err:
            answer("What is?")
        assert isinstance(err.value, ValueError)
        assert err.value.args[0] == "syntax error"

    def test_reject_two_operations_in_a_row(self) -> None:
        with pytest.raises(ValueError, match="syntax error") as err:
            answer("What is 1 plus plus 2?")
        assert isinstance(err.value, ValueError)
        assert err.value.args[0] == "syntax error"

    def test_reject_two_numbers_in_a_row(self) -> None:
        with pytest.raises(ValueError, match="syntax error") as err:
            answer("What is 1 plus 2 1?")
        assert isinstance(err.value, ValueError)
        assert err.value.args[0] == "syntax error"

    def test_reject_postfix_notation(self) -> None:
        with pytest.raises(ValueError, match="syntax error") as err:
            answer("What is 1 2 plus?")
        assert isinstance(err.value, ValueError)
        assert err.value.args[0] == "syntax error"

    def test_reject_prefix_notation(self) -> None:
        with pytest.raises(ValueError, match="syntax error") as err:
            answer("What is plus 1 2?")
        assert isinstance(err.value, ValueError)
        assert err.value.args[0] == "syntax error"

    # Additional tests for this track

    def test_4_number_question(self) -> None:
        assert answer("What is 1 plus -10 multiplied by 3 minus 4?") == -31

    def test_4_number_question_with_zero(self) -> None:
        assert answer("What is 12 minus 0 divided by 6 plus 5?") == 7

    def test_5_number_question(self) -> None:
        assert answer("What is 3 multiplied by 6 minus 2 divided by 4 plus 11?") == 15

    def test_missing_operation(self) -> None:
        with pytest.raises(ValueError, match="syntax error") as err:
            answer("What is 2 2 minus 3?")
        assert isinstance(err.value, ValueError)
        assert err.value.args[0] == "syntax error"

    def test_missing_number(self) -> None:
        with pytest.raises(ValueError, match="syntax error") as err:
            answer("What is 7 plus multiplied by -2?")
        assert isinstance(err.value, ValueError)
        assert err.value.args[0] == "syntax error"
