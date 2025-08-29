# Import random for number generation
import random

# Constants.
NUMBER_PROMPT_MESSAGE: str = "Enter a random point count: "
INVALID_INPUT_MESSAGE: str = "Please enter a valid number."

# Variables.
points_inside_circle: int = 0

# Loop until user inputs a valid number (integer).
while True:
    try:
        random_point_count = int(input(NUMBER_PROMPT_MESSAGE))
        break
    except ValueError:
        print(INVALID_INPUT_MESSAGE)

# Loop while index is less than random point count.
for _ in range(random_point_count):
    # Generate random floating point numbers for x and y between -1 and 1.
    random_x = random.uniform(-1, 1)
    random_y = random.uniform(-1, 1)
    # if x²+y² < 1 increment points inside circle.
    if random_x**2 + random_y**2 < 1:
        points_inside_circle += 1

# Calculate approximation of pi by PI~4n/N formula.
approximation_of_pi = 4 * points_inside_circle / random_point_count
# Print results.
print(f"Approximation of pi: {approximation_of_pi}")
