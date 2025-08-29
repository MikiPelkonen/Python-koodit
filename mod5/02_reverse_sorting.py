# Constants.
PROMPT: str = "Enter a number: "
RESULT_TEXT: str = "The greatest numbers in descending order: "
ERROR_MSG: str = "Please enter a valid number."
NUMBER_DISPLAY_COUNT: int = 5

# List variable for prompted numbers.
number_list: list[float] = []

# Loop until user inputs an empty string.
while True:
    user_input = input(PROMPT)
    if not user_input:
        print(RESULT_TEXT)
        break
    try:
        # Add prompted number to number list.
        number_list.append(float(user_input))
    except ValueError:
        # Ensure input is a valid number.
        print(ERROR_MSG)

# Sort number list in descending order.
number_list.sort(reverse=True)
# print results in range of 0-number display count.
for number in number_list[:NUMBER_DISPLAY_COUNT]:
    # Print results with 1 decimal precision.
    print("%.1f" % number)
