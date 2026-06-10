"""Functions for determine if a triangle is equilateral, isosceles, or scalene.
"""


type TriangleSides = tuple[float, float, float]


def is_valid_triangle(sides: TriangleSides) -> bool:
    """Determine if a triangle is a valid triangle.

    Args:
        sides (TriangleSides): Sides of the triangle.
    """

    short_side, medium_side, long_side = sorted(sides)

    return short_side + medium_side > long_side


def equilateral(sides: TriangleSides) -> bool:
    """Determine if a triangle is equilateral.

    Args:
        sides (TriangleSides): Sides of the triangle.

    Returns:
        bool: Whether triangle is a equilateral triangle.
    """
    
    return is_valid_triangle(sides) and len(set(sides)) == 1


def isosceles(sides: TriangleSides) -> bool:
    """Determine if a triangle is isosceles.

    Args:
        sides (TriangleSides): Sides of the triangle.

    Returns:
        bool: Whether triangle is a isosceles triangle.
    """
    
    return is_valid_triangle(sides) and len(set(sides)) <= 2


def scalene(sides: TriangleSides) -> bool:
    """Determine if a triangle is scalene.

    Args:
        sides (TriangleSides): Sides of the triangle.

    Returns:
        bool: Whether triangle is a scalene triangle.
    """
    
    return is_valid_triangle(sides) and len(set(sides)) == 3
