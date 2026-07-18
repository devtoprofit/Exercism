"""Function for output its input in a diamond shape.
"""

def rows(letter: str) -> list[str]:
    """Outputs its input in a diamond shape.

    Args:
        letter (str): Letter.

    Returns:
        list[str]: A diamond shape.
    """
    
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    letter_index = letters.index(letter)
    current_index = letter_index
    result: list[str] = []

    while current_index >= 0:
        part = [" "] * letter_index
        part.insert(current_index, letters[current_index])
        row = "".join(part[:: -1] + part[1:])
        current_index -= 1

        if result:
            result.insert(0, row)

        result.append(row)

    return result
