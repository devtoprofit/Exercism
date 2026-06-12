# These tests are auto-generated with test data from:
# https://github.com/exercism/problem-specifications/tree/main/exercises/isogram/canonical-data.json
# File last updated on 2023-07-19

import unittest

from isogram import (
    is_isogram,
)


class IsogramTest(unittest.TestCase):
    def test_empty_string(self) -> None:
        assert is_isogram("") is True

    def test_isogram_with_only_lower_case_characters(self) -> None:
        assert is_isogram("isogram") is True

    def test_word_with_one_duplicated_character(self) -> None:
        assert is_isogram("eleven") is False

    def test_word_with_one_duplicated_character_from_the_end_of_the_alphabet(self) -> None:
        assert is_isogram("zzyzx") is False

    def test_longest_reported_english_isogram(self) -> None:
        assert is_isogram("subdermatoglyphic") is True

    def test_word_with_duplicated_character_in_mixed_case(self) -> None:
        assert is_isogram("Alphabet") is False

    def test_word_with_duplicated_character_in_mixed_case_lowercase_first(self) -> None:
        assert is_isogram("alphAbet") is False

    def test_hypothetical_isogrammic_word_with_hyphen(self) -> None:
        assert is_isogram("thumbscrew-japingly") is True

    def test_hypothetical_word_with_duplicated_character_following_hyphen(self) -> None:
        assert is_isogram("thumbscrew-jappingly") is False

    def test_isogram_with_duplicated_hyphen(self) -> None:
        assert is_isogram("six-year-old") is True

    def test_made_up_name_that_is_an_isogram(self) -> None:
        assert is_isogram("Emily Jung Schwartzkopf") is True

    def test_duplicated_character_in_the_middle(self) -> None:
        assert is_isogram("accentor") is False

    def test_same_first_and_last_characters(self) -> None:
        assert is_isogram("angola") is False

    def test_word_with_duplicated_character_and_with_two_hyphens(self) -> None:
        assert is_isogram("up-to-date") is False
