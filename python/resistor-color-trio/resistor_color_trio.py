"""Function for represention colors as resistance value.
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


def label(colors: list[str]) -> str:
    """Function takes color names as input and output a resistance value.

    Args:
        colors (list[str]): Colors.

    Returns:
        str: Resistance value.
    """

    first_color, second_color, third_color = colors[0], colors[1], colors[2]
    resistance_value = COLORS_BAND.index(first_color) * 10 + COLORS_BAND.index(second_color)
    power = COLORS_BAND.index(third_color)

    if resistance_value % 10 == 0:
        resistance_value //= 10
        power += 1

    match power:
        case 3 | 4 | 5:
            metric_prefix = "kiloohms"
            power -= 3
        case 6 | 7 | 8:
            metric_prefix = "megaohms"
            power -= 6 
        case 9:
            metric_prefix = "gigaohms"
            power -= 9
        case _:
            metric_prefix = "ohms"

    resistance_value *= 10 ** power

    return f"{resistance_value} {metric_prefix}"   
