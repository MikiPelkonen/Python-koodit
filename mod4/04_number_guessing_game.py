import random

# Constants.
GAME_PROMPT: str = "Guess a number (1-10): "
GAME_RESULTS: dict[str, str] = {
    "high": "Too high",
    "low": "Too low",
    "correct": "Correct",
}
ERROR_MSG: str = "Invalid input! Please enter a valid integer."

# Variable for random number between 1-10
random_number: int = random.randint(1, 10)
# Initialize player guess variable with -1 to mismatch random number
player_guess: int = -1

# Loop until prompted number is equal to generated random number
while random_number != player_guess:
    try:
        player_guess = int(input(GAME_PROMPT))
        if random_number == player_guess:
            print(GAME_RESULTS["correct"])
        elif random_number > player_guess:
            print(GAME_RESULTS["low"])
        else:
            print(GAME_RESULTS["high"])
    except ValueError:
        print(ERROR_MSG)
