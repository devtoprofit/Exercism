"""Function for convert a sequence of digits.
"""


def rebase(input_base: int, digits: list[int], output_base: int) -> list[int]:
    """Convert a sequence of digits in one base into a sequence of digits in another base.

    Args:
        input_base (int): Base of a sequence of digits.
        digits (list[int]): A sequence of digits.
        output_base (int): A target base of a sequence of digits.

    Raises:
        ValueError: Input base must be >= 2.
        ValueError: Output base must be >= 2.
        ValueError: All digits must satisfy 0 <= d < input base.

    Returns:
        list[int]: A sequence of digits in target base.
    """
    
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    
    if output_base < 2:
        raise ValueError("output base must be >= 2")

    for num in digits:
        if not 0 <= num < input_base:
            raise ValueError("all digits must satisfy 0 <= d < input base")
    
    if input_base == 10:
        dec_number = int("".join([str(digit) for digit in digits]))
    else:
        dec_number = sum(num * input_base ** power for power, num in enumerate(reversed(digits)))
    
    hex_letters = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}
    result: list[int] = []

    while dec_number > 0:
        number = dec_number % output_base

        if output_base == 16 and number > 9:
            number = hex_letters[number]

        result.append(dec_number % output_base)
        dec_number //= output_base
    
    result.reverse()

    return result or [0]
