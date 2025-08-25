# Constants.
GENDER_MALE: str = "male"
GENDER_FEMALE: str = "female"
GENDER_PROMPT: str = f"Enter biological gender ({GENDER_MALE}/{GENDER_FEMALE}): "
HEMOGLOBIN_PROMPT: str = "Enter hemoglobin value (g/l): "
FEMALE_MIN_MAX_VALUES: tuple[float, float] = (117.0, 155.0)
MALE_MIN_MAX_VALUES: tuple[float, float] = (134.0, 167.0)
RESULT_TEXT: str = "Your hemoglobin is "
RESULT_OPTIONS: tuple[str, str, str] = ("low.", "high.", "normal.")
INVALID_GENDER_ERROR_TEXT: str = "Invalid gender."

# Prompt user for gender.
gender = input(GENDER_PROMPT)

# Prompt user for hemoglobin value.
# Loop until user inputs a valid number.
while True:
    try:
        hemoglobin_value = float(input(HEMOGLOBIN_PROMPT))
        break
    except ValueError:
        print("Please enter a valid number.")

# Check if gender male, female or invalid
if gender.lower() == GENDER_MALE:
    if hemoglobin_value < MALE_MIN_MAX_VALUES[0]:
        print(RESULT_TEXT + RESULT_OPTIONS[0])
    elif hemoglobin_value > MALE_MIN_MAX_VALUES[1]:
        print(RESULT_TEXT + RESULT_OPTIONS[1])
    else:
        print(RESULT_TEXT + RESULT_OPTIONS[2])
elif gender.lower() == GENDER_FEMALE:
    if hemoglobin_value < FEMALE_MIN_MAX_VALUES[0]:
        print(RESULT_TEXT + RESULT_OPTIONS[0])
    elif hemoglobin_value > FEMALE_MIN_MAX_VALUES[1]:
        print(RESULT_TEXT + RESULT_OPTIONS[1])
    else:
        print(RESULT_TEXT + RESULT_OPTIONS[2])
else:
    print(INVALID_GENDER_ERROR_TEXT)
