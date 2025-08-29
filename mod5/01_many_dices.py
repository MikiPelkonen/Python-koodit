import random

# Constants.
DICE_PROMPT: str = "How many dice to roll: "
RESULT_TEXT: str = "Sum of the dice: "
ERROR_MSG: str = "Invalid input. Please enter a valid integer."
DICE_MIN: int = 1
DICE_MAX: int = 6

# Loop until user inputs a valid integer.
while True:
    try:
        dice_count = int(input(DICE_PROMPT))
        break
    except ValueError:
        print(ERROR_MSG)

# Variable for summing dice roll results.
sum_of_dices: int = 0

# Iterate as many times as prompted dice count.
for _ in range(dice_count):
    # Add random int between dice min and dice max to sum of dices.
    sum_of_dices += random.randint(DICE_MIN, DICE_MAX)

# Print results.
print(f"{RESULT_TEXT}{sum_of_dices}")
