import random

# Constants.
FACE_COUNT_PROMPT: str = "Enter the maximum face value of the die: "
VALUE_ERROR_MSG: str = "Please enter a valid integer."


# Naming could be roll_die when rolling a single die.
def roll_dice(face_count: int) -> int:
    """
    Simulate rolling a die with custom amount of faces.

    Args:
        face_count (int): Count of faces in the die.

    Returns:
        int: Random integer between 1 and face_count.
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

# Variable for dice roll return value.
dice_roll_result: int = 0
# Loop until max face value is rolled.
while dice_roll_result != max_face_count:
    # Roll die with prompted number of faces.
    dice_roll_result = roll_dice(max_face_count)
    # Print result.
    print(dice_roll_result)
