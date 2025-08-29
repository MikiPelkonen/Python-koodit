# Constants.
LAST_NUMBER: int = 1000

# Variable for number/index
index: int = 1

# Loop while index is less than last number (1000).
while index < LAST_NUMBER:
    # Print if index is divisible by 3.
    if index % 3 == 0:
        print(index)
    # Increment index.
    index += 1
