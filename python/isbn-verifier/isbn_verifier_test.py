# These tests are auto-generated with test data from:
# https://github.com/exercism/problem-specifications/tree/main/exercises/isbn-verifier/canonical-data.json
# File last updated on 2025-12-30

import unittest

from isbn_verifier import (
    is_valid,
)


class IsbnVerifierTest(unittest.TestCase):
    def test_valid_isbn(self) -> None:
        assert is_valid("3-598-21508-8") is True

    def test_invalid_isbn_check_digit(self) -> None:
        assert is_valid("3-598-21508-9") is False

    def test_valid_isbn_with_a_check_digit_of_10(self) -> None:
        assert is_valid("3-598-21507-X") is True

    def test_check_digit_is_a_character_other_than_x(self) -> None:
        assert is_valid("3-598-21507-A") is False

    def test_invalid_check_digit_in_isbn_is_not_treated_as_zero(self) -> None:
        assert is_valid("4-598-21507-B") is False

    def test_invalid_character_in_isbn_is_not_treated_as_zero(self) -> None:
        assert is_valid("3-598-P1581-X") is False

    def test_x_is_only_valid_as_a_check_digit(self) -> None:
        assert is_valid("3-598-2X507-9") is False

    def test_only_one_check_digit_is_allowed(self) -> None:
        assert is_valid("3-598-21508-96") is False

    def test_x_is_not_substituted_by_the_value_10(self) -> None:
        assert is_valid("3-598-2X507-5") is False

    def test_valid_isbn_without_separating_dashes(self) -> None:
        assert is_valid("3598215088") is True

    def test_isbn_without_separating_dashes_and_x_as_check_digit(self) -> None:
        assert is_valid("359821507X") is True

    def test_isbn_without_check_digit_and_dashes(self) -> None:
        assert is_valid("359821507") is False

    def test_too_long_isbn_and_no_dashes(self) -> None:
        assert is_valid("3598215078X") is False

    def test_too_short_isbn(self) -> None:
        assert is_valid("00") is False

    def test_isbn_without_check_digit(self) -> None:
        assert is_valid("3-598-21507") is False

    def test_check_digit_of_x_should_not_be_used_for_0(self) -> None:
        assert is_valid("3-598-21515-X") is False

    def test_empty_isbn(self) -> None:
        assert is_valid("") is False

    def test_input_is_9_characters(self) -> None:
        assert is_valid("134456729") is False

    def test_invalid_characters_are_not_ignored_after_checking_length(self) -> None:
        assert is_valid("3132P34035") is False

    def test_invalid_characters_are_not_ignored_before_checking_length(self) -> None:
        assert is_valid("3598P215088") is False

    def test_input_is_too_long_but_contains_a_valid_isbn(self) -> None:
        assert is_valid("98245726788") is False
