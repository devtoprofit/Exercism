# These tests are auto-generated with test data from:
# https://github.com/exercism/problem-specifications/tree/main/exercises/triangle/canonical-data.json
# File last updated on 2026-02-19

import unittest

from triangle import (
    equilateral,
    isosceles,
    scalene,
)


class EquilateralTriangleTest(unittest.TestCase):

    def test_all_sides_are_equal(self) -> None:
        assert equilateral([2, 2, 2]) is True

    def test_any_side_is_unequal(self) -> None:
        assert equilateral([2, 3, 2]) is False

    def test_no_sides_are_equal(self) -> None:
        assert equilateral([5, 4, 6]) is False

    def test_all_zero_sides_is_not_a_triangle(self) -> None:
        assert equilateral([0, 0, 0]) is False

    def test_sides_may_be_floats(self) -> None:
        assert equilateral([0.5, 0.5, 0.5]) is True


class IsoscelesTriangleTest(unittest.TestCase):

    def test_last_two_sides_are_equal(self) -> None:
        assert isosceles([3, 4, 4]) is True

    def test_first_two_sides_are_equal(self) -> None:
        assert isosceles([4, 4, 3]) is True

    def test_first_and_last_sides_are_equal(self) -> None:
        assert isosceles([4, 3, 4]) is True

    def test_equilateral_triangles_are_also_isosceles(self) -> None:
        assert isosceles([4, 4, 4]) is True

    def test_no_sides_are_equal(self) -> None:
        assert isosceles([2, 3, 4]) is False

    def test_first_triangle_inequality_violation(self) -> None:
        assert isosceles([1, 1, 3]) is False

    def test_second_triangle_inequality_violation(self) -> None:
        assert isosceles([1, 3, 1]) is False

    def test_third_triangle_inequality_violation(self) -> None:
        assert isosceles([3, 1, 1]) is False

    def test_sides_may_be_floats(self) -> None:
        assert isosceles([0.5, 0.4, 0.5]) is True


class ScaleneTriangleTest(unittest.TestCase):

    def test_no_sides_are_equal(self) -> None:
        assert scalene([5, 4, 6]) is True

    def test_all_sides_are_equal(self) -> None:
        assert scalene([4, 4, 4]) is False

    def test_first_and_second_sides_are_equal(self) -> None:
        assert scalene([4, 4, 3]) is False

    def test_first_and_third_sides_are_equal(self) -> None:
        assert scalene([3, 4, 3]) is False

    def test_second_and_third_sides_are_equal(self) -> None:
        assert scalene([4, 3, 3]) is False

    def test_may_not_violate_triangle_inequality(self) -> None:
        assert scalene([7, 3, 2]) is False

    def test_sides_may_be_floats(self) -> None:
        assert scalene([0.5, 0.4, 0.6]) is True
