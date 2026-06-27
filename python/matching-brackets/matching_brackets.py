"""Function for verify that any and all brackets pairs are matched and nested correctly. 
"""

def is_paired(input_string: str) -> bool:
    """Function verify that any and all brackets pairs are matched and nested correctly. 

    Args:
        input_string (str): A string for check.

    Returns:
        bool: A given string has all brackets pairs are matched and nested correctly.
    """

    brackets = {"[": "]", "{": "}", "(": ")"}
    close_brackets = brackets.values()
    stack: list[str] = []

    for symbol in input_string:
        if symbol in brackets:
            stack.append(symbol)

        elif symbol in close_brackets:

            if len(stack) == 0:
                return False
            
            open_bracket = stack.pop()

            if symbol != brackets[open_bracket]:
                return False
    
    return len(stack) == 0
