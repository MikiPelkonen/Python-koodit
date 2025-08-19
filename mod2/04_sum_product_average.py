# Constants.
PROMPT_INDEXES: list[str] = ["first", "second", "third"]
INTEGER_COUNT: int = len(PROMPT_INDEXES)
INVALID_INTEGER_ERROR: str = "Error: Please enter a valid integer."

# Variables.
sum: int = 0
product: int = 1
average: float = 0.0

# Iterate prompt indexes.
for id in PROMPT_INDEXES:
    # Loop until user inputs an integer value.
    while True:
        try:
            # Prompt user for an integer.
            prompt_input: int = int(input(f"{'Enter the ' + id + ' integer:':30s}"))
            # Add the prompted integer value to the total sum value.
            sum += prompt_input
            # Multiply the current product value by the prompted integer value.
            product *= prompt_input
            break
        # Catch non integer inputs.
        except ValueError:
            print(INVALID_INTEGER_ERROR)

# Calculate the average.
average: float = sum / INTEGER_COUNT
# Print the results.
print("\nRESULTS:")
print(f"{'The sum of the numbers: ':30s}{sum}")
print(f"{'The product of the numbers: ':30s}{product}")
print(f"{'The average of the numbers: ':30s}{average}")
