"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it's memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""
from typing import Any

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 4


def sublist(list_one: list[Any], list_two: list[Any]) -> int:
    """Determine the sublist category.

    Args:
        list_one (list[Any]): First list for compare.
        list_two (list[Any]): Second list for compare.

    Returns:
        int: Sublist category.
    """
    
    if list_one == list_two:
        return EQUAL
    
    if not list_one:
        return SUBLIST
    
    if not list_two:
        return SUPERLIST
    
    if len(list_one) < len(list_two):
        inner_list, outer_list = list_one[:], list_two[:]
        category = SUBLIST
    else:
        inner_list, outer_list = list_two[:], list_one[:]
        category = SUPERLIST
    
    len_inner_list = len(inner_list)

    while inner_list[0] in outer_list:
        start_index = outer_list.index(inner_list[0])
        outer_list = outer_list[start_index:]

        if len_inner_list <= len(outer_list):

            if inner_list == outer_list[:len_inner_list]:
                return category
            
            outer_list = outer_list[1:]

        else:
            break
    
    return UNEQUAL
