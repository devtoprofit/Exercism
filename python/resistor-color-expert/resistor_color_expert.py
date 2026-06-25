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

TOLERANCE_BAND: dict[str, float] = {
    "grey": 0.05,
    "violet": 0.1,
    "blue": 0.25,
    "green": 0.5,
    "brown": 1,
    "red": 2,
    "gold": 5,
    "silver": 10
}


def resistor_label(colors: list[str]) -> str:
    """Function takes color names as input and output a resistance value.

    Args:
        colors (list[str]): Colors.

    Returns:
        str: Resistance value.
    """

    if len(colors) == 1:
        resistance = COLORS_BAND.index(colors[0])
        return f"{resistance} ohms"

    resistance_colors = reversed(colors[:-2])
    resistance = sum(COLORS_BAND.index(color) * 10 ** power
                        for power, color in enumerate(resistance_colors))
    
    power = COLORS_BAND.index(colors[-2])
    resistance *= 10 ** power

    if resistance >= 10 ** 9:
        resistance /= 10 ** 9
        prefix = "giga"

    elif resistance >= 10 ** 6:
        resistance /= 10 ** 6
        prefix = "mega"

    elif resistance >= 10 ** 3:
        resistance /= 10 ** 3
        prefix = "kilo"

    else:
        prefix = ""

    if resistance == int(resistance):
        resistance = int(resistance)    

    tolerance = f" ±{TOLERANCE_BAND[colors[-1]]}%"

    return f"{resistance} {prefix}ohms{tolerance}"
