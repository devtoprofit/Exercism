# These tests are auto-generated with test data from:
# https://github.com/exercism/problem-specifications/tree/main/exercises/pangram/canonical-data.json
# File last updated on 2023-07-19

import unittest

from pangram import (
    is_pangram,
)


class PangramTest(unittest.TestCase):
    def test_empty_sentence(self) -> None:
        assert is_pangram("") is False

    def test_perfect_lower_case(self) -> None:
        assert is_pangram("abcdefghijklmnopqrstuvwxyz") is True

    def test_only_lower_case(self) -> None:
        assert is_pangram("the quick brown fox jumps over the lazy dog") is True

    def test_missing_the_letter_x(self) -> None:
        assert is_pangram("a quick movement of the enemy will jeopardize five gunboats") is False

    def test_missing_the_letter_h(self) -> None:
        assert is_pangram("five boxing wizards jump quickly at it") is False

    def test_with_underscores(self) -> None:
        assert is_pangram("the_quick_brown_fox_jumps_over_the_lazy_dog") is True

    def test_with_numbers(self) -> None:
        assert is_pangram("the 1 quick brown fox jumps over the 2 lazy dogs") is True

    def test_missing_letters_replaced_by_numbers(self) -> None:
        assert is_pangram("7h3 qu1ck brown fox jumps ov3r 7h3 lazy dog") is False

    def test_mixed_case_and_punctuation(self) -> None:
        assert is_pangram('"Five quacking Zephyrs jolt my wax bed."') is True

    def test_a_m_and_a_m_are_26_different_characters_but_not_a_pangram(self) -> None:
        assert is_pangram("abcdefghijklm ABCDEFGHIJKLM") is False

    # Additional tests for this track

    def test_sentence_without_lower_bound(self) -> None:
        assert is_pangram("bcdefghijklmnopqrstuvwxyz") is False

    def test_sentence_without_upper_bound(self) -> None:
        assert is_pangram("abcdefghijklmnopqrstuvwxy") is False
