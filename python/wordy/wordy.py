"""Function for parse and evaluate simple math word problems returning the answer as an integer.
"""

from operator import add, floordiv, mul, sub


def answer(question: str) -> int:
    """Parse and evaluate simple math word problems returning the answer as an integer.

    Args:
        question (str): Simple math word problem.

    Raises:
        ValueError: Syntax error.
        ValueError: Unknown operation.

    Returns:
        int: The answer as an integer.
    """
    
    question_start = "What is "
    expression = ""

    if question.startswith(question_start):
        expression = f"plus {question.removeprefix("What is ").removesuffix("?")}"
    else:
        raise ValueError("syntax error")
    
    operations = {
        "plus": add,
        "minus": sub,
        "multiplied by": mul,
        "divided by": floordiv
    }

    result = 0

    while expression:
        current_operator = None

        for operation, operator in operations.items():
            if expression.startswith(operation):
                expression = expression.removeprefix(operation).lstrip()
                current_operator = operator
                break
               
        if not current_operator:
            if expression[0].isalpha():
                raise ValueError("unknown operation")
            
            raise ValueError("syntax error")

        digits = ""
        first_digit = True

        for letter in expression:
            if letter.isdigit() or (first_digit and letter == "-"):
                digits += letter
                first_digit = False
            else:
                break
        
        if not digits:
            raise ValueError("syntax error")

        expression = expression.removeprefix(digits).lstrip()
        operand = int(digits)
        result = current_operator(result, operand)

    return result
