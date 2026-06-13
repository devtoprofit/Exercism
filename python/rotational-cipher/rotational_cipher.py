"""Implementation of the rotational cipher, also sometimes called the Caesar cipher.
"""

from string import ascii_lowercase, ascii_uppercase


def rotate(text: str, key: int) -> str:
    """Rotational cipher.

    Args:
        text (str): Text to transform.
        key (int): The letter is shifted for as many values as the value of the key.

    Returns:
        str: Encoded text.
    """

    alphabet = ascii_uppercase + ascii_lowercase
    rot_alphabet = (ascii_uppercase[key:] + ascii_uppercase[:key]
                      + ascii_lowercase[key:] + ascii_lowercase[:key])
    translation_table = str.maketrans(alphabet, rot_alphabet)

    return text.translate(translation_table)
