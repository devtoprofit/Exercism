"""Function for validate book identification numbers.
"""


def is_valid(isbn: str) -> bool:
    """Validate book identification numbers.

    Args:
        isbn (str): ISBN for check.

    Returns:
        bool: True - if ISBN is valid, otherwise False.
    """

    clean_isbn = isbn.replace("-", "")

    if len(clean_isbn) != 10:
        return False
    
    check_sum = 0

    for factor, letter in enumerate(clean_isbn[:: -1], 1):
        
        digit = "10" if factor == 1 and letter == "X" else letter
        
        if not digit.isdigit():
            return False
        
        check_sum += int(digit) * factor
    
    return check_sum % 11 == 0
