"""Function to convert a number into its corresponding raindrop sounds.
"""


def convert(number: int) -> str:
    """Convert a number into its corresponding raindrop sounds.

    Args:
        number (int): number for convert

    Returns:
        str: _description_
    """

    result = ""

    if number % 3 == 0:
        result += "Pling"
    
    if number % 5 == 0:
        result += "Plang"
    
    if number % 7 == 0:
        result += "Plong"
    
    if not result:
        result = str(number)
    
    return result
