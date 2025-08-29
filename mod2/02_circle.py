# Import pi from math library
from math import pi

# Loop until user inputs a valid number.
while True:
    try:
        radius = float(input("Enter the radius of the circle: "))
        # Break loop on valid number.
        break
    except ValueError:
        # Catch non number input error and print error msg.
        print("Invalid input! Please enter an integer or a floating point number.")

# Calculate circle area with formula: PIr².
area = pi * (radius**2)

# Print results.
print(f"The area of the circle is {area}")
