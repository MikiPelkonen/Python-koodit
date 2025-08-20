# Constants.
PROMPT_INDEXES: list[str] = ["first", "second", "third"]
INTEGER_COUNT: int = len(PROMPT_INDEXES)
INVALID_INTEGER_ERROR: str = "Error: Please enter a valid integer."

# Variables.
num1: int = 0
num2: int = 0
num3: int = 0
sum_of_numbers: int = 0
product_of_numbers: int = 1
average_of_numbers: float = 0.0

# Iterate prompt indexes.
for idx, name in enumerate(PROMPT_INDEXES):
    # Loop until user inputs an integer value.
    while True:
        try:
            # Prompt user for an integer.
            prompt_input: int = int(input(f"Enter the {name} integer: "))
            if idx == 0:
                num1 = prompt_input
            elif idx == 1:
                num2 = prompt_input
            else:
                num3 = prompt_input

            # Add the prompted integer value to sum of number
            sum_of_numbers += prompt_input
            # Multiply the current product of numbers by the prompted integer value.
            product_of_numbers *= prompt_input
            break
        # Catch non integer inputs.
        except ValueError:
            print(INVALID_INTEGER_ERROR)

# Calculate the average_of_numbers.
average_of_numbers: float = sum_of_numbers / INTEGER_COUNT
# Print the results.
print(f"The sum of the numbers: {sum_of_numbers}")
print(f"The product of the numbers: {product_of_numbers}")
print(f"The average of the numbers: {average_of_numbers}")
