"""Functions:
- to look up the numerical value associated with a particular color band;
- to list the different band colors.
"""


def color_code(color: str) -> int:
    """Determine the numerical value associated with a particular color band.

    Args:
        color (str): Color.

    Returns:
        int: The numerical value associated with a color band.
    """

    return colors().index(color)


def colors() -> list[str]:
    """Determine the list of different band colors.

    Returns:
        list[str]: The list of different band colors.
    """

    return [
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
