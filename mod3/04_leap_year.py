# Constants.
YEAR_PROMPT: str = "Enter a year: "
INVALID_NUMBER_ERROR: str = "Please input a valid number."

# Prompt user for a year.
# Loop until user inputs a valid number (integer).
while True:
    try:
        year = int(input(YEAR_PROMPT))
        break
    except ValueError:
        print(INVALID_NUMBER_ERROR)

# Evaluate if year is divisible by 4 and not divisible by 100 or year is divisible by 400.
is_leap_year: bool = (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

# Print results.
print(f"{year} {'is' if is_leap_year else 'is not'} a leap year.")
