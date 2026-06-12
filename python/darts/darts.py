"""Function for calculate the points scored in a single toss of a Darts game.
"""


def score(x: float, y: float) -> int:
    """Calculate the points scored in a single toss of a Darts game.

    Args:
        x (float): Coordinate.
        y (float): Coordinate.

    Returns:
        int: Scored points.
    """

    radius = (x ** 2 + y ** 2) ** 0.5

    if radius <= 1:
        points = 10
    elif radius <= 5:
        points = 5
    elif radius <= 10:
        points = 1
    else:
        points = 0

    return points
