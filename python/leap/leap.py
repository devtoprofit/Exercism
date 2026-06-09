"""Function to determine whether a given year is a leap year.
"""


def leap_year(year: int) -> bool:
    """Determine whether a given year is a leap year.

    Args:
        year (int): Year for check.

    Returns:
        bool: Whether a given year is a leap year.
    """
    
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0
