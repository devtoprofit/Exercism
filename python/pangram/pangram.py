"""Function for determine if a sentence is a pangram.
"""


def is_pangram(sentence: str) -> bool:
    """Determine if a sentence is a pangram.

    Args:
        sentence (str): Sentence for check.

    Returns:
        bool: True - if a sentence is a pangram, otherwise False.
    """

    return len({char for char in sentence.lower() if char.isalpha()}) == 26
