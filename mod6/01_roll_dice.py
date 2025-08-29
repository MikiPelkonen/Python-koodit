# Import random for random number generation.
import random


# Naming could be roll_die when rolling a single die.
def roll_dice():
    """
    Simulate rolling a six-sided die.

    Returns:
        int: An integer between 1 and 6.
    """
    return random.randint(1, 6)


# Main program.
# Int variable to hold dice roll return value.
dice_roll_result: int = 0
# Loop until dice roll return value is number 6.
while dice_roll_result != 6:
    # Roll.
    dice_roll_result = roll_dice()
    # Print result.
    print(dice_roll_result)
