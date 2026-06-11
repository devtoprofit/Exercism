"""Functions to translate text from English to Pig Latin.
"""


SUFFIX = "ay"
VOWELS = ["a", "e", "i", "o", "u"]


def translate_word(word: str) -> str:
    """Translate word from English to Pig Latin.

    Args:
        word (str): English word.

    Returns:
        str: Word in Pig Latin.
    """

    if word.startswith(("xr", "yt")):
        return word + SUFFIX
    
    prefix = ""
    prefix_length = 0

    for letter in word:
        
        if letter == "u" and prefix.endswith("q"):
            prefix_length += 1
            break

        if (letter == "y" and prefix_length > 0) or letter in VOWELS:
            break

        prefix += letter
        prefix_length += 1

    return word[prefix_length:] + word[:prefix_length] + SUFFIX


def translate(text: str) -> str:
    """Translate text from English to Pig Latin.

    Args:
        word (str): English text.

    Returns:
        str: Text in Pig Latin.
    """

    words = text.split()
    return " ".join([translate_word(word) for word in words])
