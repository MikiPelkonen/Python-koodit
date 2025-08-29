"""
File: 02_roll_custom_dice.py

Description:
    Prompts user for custom options for a die.
    Simulates rolling the die until maximum face value is rolled.
    Prints every result.

Functions:
    roll_dice(face_count: int) -> int:
        Returns a random integer between 1 and `face_count`.

Example:
    >>> Enter the maximum face value of the die: 21
    >>> roll_dice(21)
    5
    >>> roll_dice(21)
    21

Author: Miki Pelkonen
Date: 2025-08-29
"""

import random

# Constants.
FACE_COUNT_PROMPT: str = "Enter the maximum face value of the die: "
VALUE_ERROR_MSG: str = "Please enter a valid integer."


# Naming could be roll_die when rolling a single die.
def roll_dice(face_count: int) -> int:
    """
    Simulates rolling a die with custom amount of faces.

    Args:
        face_count (int): Count of faces in the die.

    Returns:
        int: Random integer between 1 and `face_count`.
    """
    return random.randint(1, face_count)


# Main program.
# Loop until user inputs a valid integer.
while True:
    try:
        max_face_count = int(input(FACE_COUNT_PROMPT))
        break
    except ValueError:
        print(VALUE_ERROR_MSG)

dice_roll_result: int = 0
# Loop until max face value is rolled.
while dice_roll_result != max_face_count:
    # Roll die with prompted number of faces.
    dice_roll_result = roll_dice(max_face_count)
    # Print result.
    print(dice_roll_result)
