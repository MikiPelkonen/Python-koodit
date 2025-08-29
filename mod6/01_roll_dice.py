"""
File: 01_roll_dice.py

Description:
    Simulates rolling a six-sided die until a six is rolled.
    Prints each roll value.

Functions:
    roll_dice():
        Simulates rolling a six-sided die and returns result.

Example:
    >>> roll_dice()
    4
    >>> roll_dice()
    6

Author: Miki Pelkonen
Date: 2025-08-29
"""

# Import random for random number generation.
import random


# Functions.
# Naming could be roll_die when rolling a single die.
def roll_dice():
    """
    Simulate rolling a six-sided die.

    Returns:
        int: An integer between 1 and 6.
    """
    return random.randint(1, 6)


# Main program.
dice_roll_result: int = 0
# Loop until dice roll return value is number 6.
while dice_roll_result != 6:
    # Roll.
    dice_roll_result = roll_dice()
    # Print result.
    print(dice_roll_result)
