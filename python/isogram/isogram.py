"""Function for determine if a word or phrase is an isogram.
"""


def is_isogram(string: str) -> bool:
    """Determine if a word or phrase is an isogram.

    Args:
        string (str): Word or phrase for check.

    Returns:
        bool: True - if a word is a isogram, otherwise False.
    """

    letters = string.replace(" ", "").replace("-", "").lower()
    return len(letters) == len(set(letters))
