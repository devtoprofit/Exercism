"""Function for determine whether a number is an Armstrong number.
"""


def is_armstrong_number(number: int) -> bool:
    """Determine whether a number is an Armstrong number.

    Args:
        number (int): Number for determine.  

    Returns:
        bool: Whether a number is an Armstrong number.
    """
    
    current_number = number
    digits: list[int] = []

    while current_number > 0:
        digit = current_number % 10
        digits.append(digit)
        current_number //= 10
        
    power = len(digits)
    armstrong_number = sum([digit ** power for digit in digits])

    return number == armstrong_number
