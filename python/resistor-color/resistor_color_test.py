# These tests are auto-generated with test data from:
# https://github.com/exercism/problem-specifications/tree/main/exercises/resistor-color/canonical-data.json
# File last updated on 2023-07-19

import unittest

from resistor_color import (
    color_code,
    colors,
)


class ResistorColorTest(unittest.TestCase):
    def test_black(self) -> None:
        assert color_code("black") == 0

    def test_white(self) -> None:
        assert color_code("white") == 9

    def test_orange(self) -> None:
        assert color_code("orange") == 3

    def test_colors(self) -> None:
        expected = [
            "black",
            "brown",
            "red",
            "orange",
            "yellow",
            "green",
            "blue",
            "violet",
            "grey",
            "white",
        ]
        assert colors() == expected
