# Constants.
LOT_IN_GRAMS: float = 13.3
POUND_IN_GRAMS: float = LOT_IN_GRAMS * 32
TALENT_IN_GRAMS: float = POUND_IN_GRAMS * 20
PROMPT_INDEXES: list[str] = ["talents", "pounds", "lots"]
PROMPT_INDEX_COUNT: int = len(PROMPT_INDEXES)
VALUE_ERROR_MSG: str = "Invalid input. Please enter a number."

# Variables.
measure_list: list[float] = [0.0] * PROMPT_INDEX_COUNT
total_grams: float = 0.0
remaining_grams: float = 0.0
kilograms: int = 0

# Iterate promp indexes.
for idx, name in enumerate(PROMPT_INDEXES):
    # Loop until user inputs a valid number.
    while True:
        try:
            # Store prompted number value to list of floats.
            measure_list[idx] = float(input(f"Enter {name}: "))
            break
        except ValueError:
            print(VALUE_ERROR_MSG)

# Unpack list to variables.
talents, pounds, lots = measure_list
# Calculate total grams.
total_grams = (
    (TALENT_IN_GRAMS * talents) + (POUND_IN_GRAMS * pounds) + (LOT_IN_GRAMS * lots)
)
# Calculate full kilograms.
kilograms: int = (total_grams / 1000).__floor__()
# Calculate remaining grams.
remaining_grams = total_grams - kilograms * 1000

# Print results.
print(
    f"The weight in modern units:\n{kilograms} kilograms and {remaining_grams:.2f} grams."
)
