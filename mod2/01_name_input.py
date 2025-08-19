# Store empty string variable for name input
name = ""

# Loop while user input is empty string or whitespaces only
# Strip leading and trailing whitespaces
while not name:
    name = input("Give name: ").strip()
    if not name:
        print("Error: Name needs to contain character(s).\nEnter a valid name.")

# Capitalize name
greeting = f"Hello, {name.capitalize()}."

print(greeting)
