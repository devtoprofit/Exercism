"""Function for represention colors as number.
"""

COLORS_BAND = [
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


def value(colors: list[str]) -> int:
    """Function takes color names as input and output a two digit number,
    even if the input is more than two colors!

    Args:
        colors (list[str]): Colors.

    Returns:
        int: A number representing value of colors.
    """
    return COLORS_BAND.index(colors[0]) * 10 + COLORS_BAND.index(colors[1])
