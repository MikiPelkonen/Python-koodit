# Import isqrt from math that returns floor value of number squareroot.
from math import isqrt

# Constants.
PROMPT: str = "Enter an integer: "
VALUE_ERROR_MSG: str = "Please enter a valid integer."
RESULT_MESSAGES: tuple[str, str] = "is a prime number.", "is not a prime number."

# Loop until user inputs a valid integer.
while True:
    try:
        user_input = int(input(PROMPT))
        break
    except ValueError:
        print(VALUE_ERROR_MSG)

# Boolean variable for prime check result.
# Initialize with True value.
is_prime: bool = True

# If prompted number is 1, 0 or negative number => not a prime number.
if user_input <= 1:
    is_prime = False
# Only number 2 is prime even number.
elif user_input % 2 == 0:
    is_prime = user_input == 2
else:
    # Loop in range 2 -> square root of prompted number.
    for i in range(2, isqrt(user_input) + 1):  # + 1 to include square root itself.
        # If prompted number is divisible by loop index number => not prime.
        if user_input % i == 0:
            is_prime = False
            break  # Break early on false condition.

# Print result.
print(f"{user_input} {RESULT_MESSAGES[0 if is_prime else 1]}")
