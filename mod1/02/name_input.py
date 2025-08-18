# Store empty string variable for name input
name = ""

# Loop while user input is empty string or whitespaces only
# Strip leading and trailing whitespaces
while not name:
    name = input("Input your name: ").strip()
    if not name:
        print("Error: Name needs to contain character(s).\nEnter a valid name.")

# Capitalize name
print(f"Greetings, {name.capitalize()}.")
