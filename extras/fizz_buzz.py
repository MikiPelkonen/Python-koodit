"""
File: fizz_buzz.py

Description:
    Implementation of the classic fizzbuzz problem.

Functions:
    fizz_buzz(number: int):

Author: Miki Pelkonen
Date: 2025-09-01
"""

# Constants.
FIZZ_BUZZ: tuple[str, str] = "fizz", "buzz"


# Functions.
def fizz_buzz(number: int):
    """
    Print "fizz" if divisible by 3, "buzz" if divisible by 5,
    "fizzbuzz" if divisible by both, otherwise the number.

    Args:
        number (int): Number to evaluate.
    """
    to_print: str = ""
    if number % 3 == 0:
        to_print += FIZZ_BUZZ[0]
    if number % 5 == 0:
        to_print += FIZZ_BUZZ[1]
    print(to_print or number)


# Main program.
# Runs fizz_buzz for numbers 1 through 100.
for n in range(1, 101):
    fizz_buzz(n)

