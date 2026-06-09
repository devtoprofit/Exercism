"""Function for determine the number of steps it takes to
reach 1 according to the rules of the Collatz Conjecture.
"""


def steps(number: int) -> int:
    """Determine the number of steps it takes to
    reach 1 according to the rules of the Collatz Conjecture.

    Args:
        number (int): Only positive integers are allowed.

    Raises:
        ValueError: Positive integer to determine the number of steps.

    Returns:
        int: The number of steps to reach 1.
    """

    if number < 1:
        raise ValueError("Only positive integers are allowed")
    
    count = 0

    while number > 1:
        count += 1

        if number % 2 == 0:
            number //= 2
        else:
            number = number * 3 + 1
    
    return count
