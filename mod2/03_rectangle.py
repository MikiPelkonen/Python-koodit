# Constant tuple of strings for rectangle dimension names
DIMENSIONS = "length", "width"

# Empty list for prompted length and width
result_list = []
# Loop dimensions
for dimension in DIMENSIONS:
    while True:
        try:
            # Prompt for rectangle dimension value by given dimension name.
            value = float(input(f"Enter the {dimension} of the rectangle: "))
            # Ensure positive numbers.
            if value < 0:
                print(f"Rectangle {dimension} must be a positive number.")
                continue
            # Add to result list.
            result_list.append(value)
            break
        # Catch value error.
        except ValueError:
            print("Please enter a valid number.")

# Unpack list to variables.
length, width = result_list
# Calculate perimeter from given length and width.
perimeter = 2 * (length + width)
# Calculate area from given length and width.
area = length * width

# Print results.
print(f"The perimeter of the rectangle is {perimeter}")
print(f"The area of the rectangle is {area}")
