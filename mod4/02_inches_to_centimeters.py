# Constants.
PROMPT: str = "Enter length in inches (negative value to quit): "
VALUE_ERROR_MESSAGE: str = "Please enter a valid number."

# Prompt user for input and break loop when input is negative number.
# Ensure input is a number.
while True:
    try:
        inches = float(input(PROMPT))
        if inches < 0:
            break
        print(f"{inches:.1f} inches is {(inches * 2.54):.2f} centimeters")
    except ValueError:
        print(VALUE_ERROR_MESSAGE)

print("Program ended.")
