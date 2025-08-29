"""
File: 04_summing_list.py

Description:
    Sums the values of an integer list and prints the result.

Functions:
    sum_of_list(int_list: list[int]) -> int:
        Returns the sum of listed values.

Example:
    >>> sum_of_list([1, 4, 7, 3])
    15

Author: Miki Pelkonen
Date: 2025-08-29
"""

# Constants.
TEST_INTEGER_LIST: list[int] = [1, 4, 7, 3]
RESULT_PREFIX: str = "The sum of the numbers in the list is: "


# Functions.
def sum_of_list(int_list: list[int]) -> int:
    """
    Sums the values of an integer list.

    Args:
        int_list (list[int): List of integers.
    Returns:
        int: Sum of `int_list`
    """
    return sum(int_list)


# Main program.
print(f"{RESULT_PREFIX}{sum_of_list(TEST_INTEGER_LIST)}")
