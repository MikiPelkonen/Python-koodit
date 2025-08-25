# Constants
ZANDER_LENGTH_PROMPT: str = "Enter the length of the zander in centimeters: "
ZANDER_SUCCESS_TEXT: str = "The zander meets the size limit."
ZANDER_FAILURE_TEXT: str = "The zander does not meet the size limit.\nPlease release the fish back into the lake."
MIN_ZANDER_LENGTH: float = 42.0

# Loop until user inputs a valid number
while True:
    try:
        zander_length = float(input(ZANDER_LENGTH_PROMPT))
        break
    except ValueError:
        print("Invalid value entered. Please enter a valid number.")

# Evaluate if user input is greater or equal as min zander length
if zander_length >= MIN_ZANDER_LENGTH:
    # Greater or equal print success text
    print(ZANDER_SUCCESS_TEXT)
else:
    # Less than print failure text
    print(ZANDER_FAILURE_TEXT)
    # Calculate the difference in zander and min zander length
    length_difference = MIN_ZANDER_LENGTH - zander_length
    # Print the the length difference with 1 decimal accuracy
    print(f"The fish was {length_difference:.1f} centimeters below the size limit.")
