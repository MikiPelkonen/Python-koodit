from math import pi

while True:
    try:
        radius = float(input("Enter circle radius: "))
        break
    except ValueError:
        print("Invalid input! Please enter integer or floating point number")

area_circle = pi * (radius**2)
print(f"Area of circle with radius: {radius} is: {area_circle}")
