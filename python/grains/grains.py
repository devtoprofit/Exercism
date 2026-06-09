"""Functions for calculating the number of grains of wheat on a chessboard.
"""


MIN_SQUARE = 1
MAX_SQUARE = 64
RATIO = 2


def square(number: int) -> int:
    """Calculate the number of grains on a given square.

    Args:
        number (int): Square's number.

    Raises:
        ValueError: Square must be between MIN_SQUARE and MAX_SQUARE.

    Returns:
        int: The number of grains.
    """

    if number < MIN_SQUARE or number > MAX_SQUARE:
        raise ValueError(f"square must be between {MIN_SQUARE} and {MAX_SQUARE}")
    
    return RATIO ** (number - 1)


def total() -> int:
    """Calculate the total number of grains on the chessboard.

    Returns:
        int: The total number of grains.
    """

    return MIN_SQUARE * (1 - RATIO ** MAX_SQUARE) // (1 - RATIO)
