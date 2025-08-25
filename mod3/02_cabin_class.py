# Constants.
CABIN_CLASS_PROMPT: str = "Enter the cabin class (LUX, A, B, or C): "

# Prompt user for input
user_input = input(CABIN_CLASS_PROMPT)

# If else madness for checking user input
if user_input == "LUX":
    print("Upper-deck cabin with a balcony.")
elif user_input == "A":
    print("Above the car deck, equipped with a window.")
elif user_input == "B":
    print("Windowless cabin above the car deck.")
elif user_input == "C":
    print("Windowless cabin below the car deck.")
else:
    print("Invalid cabin class.")
