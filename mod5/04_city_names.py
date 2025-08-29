# Constants.
CITY_TOTAL_COUNT: int = 5
PROMPT: str = "Enter the name of a city: "
RESULT_HEADING: str = "\n\nThe cities you entered: "

# String list variable for storing prompted city names.
# Initialize with empty string times city total count.
city_names: list[str] = [""] * CITY_TOTAL_COUNT

# Loop in range of city names list length.
for i in range(len(city_names)):
    # Store prompted city name in list.
    city_names[i] = input(PROMPT)

# Print result heading.
print(RESULT_HEADING)
for city in city_names:
    # Print every city name capitalized in the list.
    print(city.capitalize())
