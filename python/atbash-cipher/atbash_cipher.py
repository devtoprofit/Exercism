"""An implementation of the Atbash cipher,
an ancient encryption system created in the Middle East.
"""

from string import ascii_lowercase

PLAIN = ascii_lowercase
CIPHER = ascii_lowercase[::-1]


def encode(plain_text: str) -> str:
    """Encode a given text.

    Args:
        plain_text (str): Text for encode.

    Returns:
        str: Encoded text.
    """

    text = ""

    for letter in plain_text.lower():
        if letter.isalnum():
            text += letter

    translation_table = str.maketrans(PLAIN, CIPHER)
    text = text.translate(translation_table)
    
    return " ".join([text[index: index + 5] for index in range(0, len(text), 5)])


def decode(ciphered_text: str) -> str:
    """Decode a given text.

    Args:
        ciphered_text (str): Text for decode.

    Returns:
        str: Decoded text.
    """
    
    translation_table = str.maketrans(CIPHER, PLAIN)
    text = ciphered_text.replace(" ", "")

    return text.translate(translation_table)
