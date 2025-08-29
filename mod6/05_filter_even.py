"""
File: 05_filter_even.py

Description:
    Creates a list of integers.
    Creates another list with only even numbers from previous list.
    Prints the results of both lists.

Functions:
    filter_even_numbers(original_list: list[int]) -> list[int]:
        Returns list with only even numbers from `original_list`.

Example:
    >>> filter_even_numbers([1, 2, 3, 4])
    [2, 4]

Author: Miki Pelkonen
Date: 2025-08-29
"""

# Constants.
ORIGINAL_LIST: list[int] = [n for n in range(1, 11)]


# Functions.
def filter_even_numbers(original_list: list[int]) -> list[int]:
    """
    Filter and return even numbers from an integer list.

    Args:
        original_list (list[int]): A list of integers.

    Returns:
        list[int]: Even numbers from `original_list`.
    """
    return [n for n in original_list if n % 2 == 0]


# Main program.
filtered_list = filter_even_numbers(ORIGINAL_LIST)
print(f"Original list: {ORIGINAL_LIST}")
print(f"List with even numbers only: {filtered_list}")
