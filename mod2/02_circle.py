# Import pi from math library
from math import pi

# Loop until user inputs a number
while True:
    try:
        radius = float(input("Enter circle radius: "))
        break
    except ValueError:
        print("Invalid input! Please enter integer or floating point number")

# Calculate circle area
area_circle = pi * (radius**2)

print(f"Area of circle with radius: {radius} is: {area_circle}")
