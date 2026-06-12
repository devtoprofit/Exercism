"""Function for determine if a number is perfect.
"""


def classify(number: int) -> str:
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")
    
    aliquot_sum = sum(num for num in range(1, number) if number % num == 0)

    if number == aliquot_sum:
        category = "perfect"
    elif number < aliquot_sum:
        category = "abundant"
    else:
        category = "deficient"

    return category
