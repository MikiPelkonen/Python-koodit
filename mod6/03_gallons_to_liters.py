"""
File: 03_gallons_to_liters.py

Description:
    Converts fuel volumes from US gallons to liters.
    The program repeatedly prompts user for a volume in gallons to convert.
    Entering a negative value exists the program.

Functions:
    gallons_to_liters(gallons: float) -> float:
        Converts gallons to liters.

Example:
    >>> Enter a volume in American gallons (negative value to quit): 10
    >>> gallons_to_liters(10)
    37.85
    >>> Enter a volume in American gallons (negative value to quit): -1
    Program finished.

Author: Miki Pelkonen
Date: 2025-08-29
"""

# Constants.
GALLON_IN_LITERS: float = 3.785
GALLONS_VOLUME_PROMPT: str = (
    "Enter a volume in American gallons (negative value to quit): "
)
VALUE_ERROR_MSG: str = "Please enter a valid floating point number."
PROGRAM_FINISHED_MSG: str = "Program finished."


# Functions.
def gallons_to_liters(gallons: float) -> float:
    """
    Converts US gallons to liters and returns the value.

    Args:
        gallons (float): Volume in gallons.
    Returns:
        float: `gallons` multiplied by `GALLON_IN_LITERS`.
    """
    return gallons * GALLON_IN_LITERS


# Main program.
prompted_gallons: float = 0.0

while True:
    try:
        prompted_gallons = float(input(GALLONS_VOLUME_PROMPT))
        if prompted_gallons < 0:
            print(PROGRAM_FINISHED_MSG)
            break
        print(
            f"{prompted_gallons} American gallons is {gallons_to_liters(prompted_gallons):.2f} liters."
        )
    except ValueError:
        print(VALUE_ERROR_MSG)
