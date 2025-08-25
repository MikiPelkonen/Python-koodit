# Constants.
PROMPT = "Enter a number (or press Enter to quit): "
VALUE_ERROR_MSG = "Please input a valid number."

# float list to hold prompted numbers.
list_of_numbers: list[float] = []

# Loop until input is an empty string.
while True:
    user_input = input(PROMPT)
    if not user_input:
        break
    try:
        number = float(user_input)
        list_of_numbers.append(number)
    except ValueError:
        print(VALUE_ERROR_MSG)

# Get smallest and greatest value from list with built in functions.
min = min(list_of_numbers)
max = max(list_of_numbers)

# Print results with 1 decimal accuracy.
print(f"Smallest number: {min:.1f}\nLargest number: {max:.1f}")
