# Import pi from math library
from math import pi

# Loop until user inputs a number
while True:
    try:
        radius = float(input("Enter the radius of the circle: "))
        break
    except ValueError:
        print("Invalid input! Please enter an integer or a floating point number.")

# Calculate circle area
area = pi * (radius**2)

print(f"The area of the circle is {area}")
