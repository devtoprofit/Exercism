# These tests are auto-generated with test data from:
# https://github.com/exercism/problem-specifications/tree/main/exercises/resistor-color-duo/canonical-data.json
# File last updated on 2023-07-19

import unittest

from resistor_color_duo import (
    value,
)


class ResistorColorDuoTest(unittest.TestCase):
    def test_brown_and_black(self) -> None:
        assert value(["brown", "black"]) == 10

    def test_blue_and_grey(self) -> None:
        assert value(["blue", "grey"]) == 68

    def test_yellow_and_violet(self) -> None:
        assert value(["yellow", "violet"]) == 47

    def test_white_and_red(self) -> None:
        assert value(["white", "red"]) == 92

    def test_orange_and_orange(self) -> None:
        assert value(["orange", "orange"]) == 33

    def test_ignore_additional_colors(self) -> None:
        assert value(["green", "brown", "orange"]) == 51

    def test_black_and_brown_one_digit(self) -> None:
        assert value(["black", "brown"]) == 1
