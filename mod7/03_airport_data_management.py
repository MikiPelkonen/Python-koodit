"""
File: 03_airport_data_management.py

Description:
    A simple program for managing airport data.
    Options:
        1. Add airport
        2. Fetch airport
        3. Quit

Functions:
    add_airport(icao: str, name: str):
    get_airport_by_icao(icao: str) -> str:
    manage_airport_data():

Example:
    >>> Please choose an option (1-3): 1
    >>> Enter the ICAO code: FGFG
    >>> Enter the airport name: Temp airport
    Airport Temp airport with ICAO code FGFG has been added.
    >>> Please choose an option(1-3): 2
    >>> Enter the ICAO code: FGFG
    The airport with ICAO code FGFG is Temp airport.

Author: Miki Pelkonen
Date: 2025-09-02
"""

# Constants.
PROMPT_HEADING: str = "\nAirport Data Management"
AIRPORT_DATA_PROMPTS: tuple[str, str] = (
    "Enter the ICAO code: ",
    "Enter the airport name: ",
)
OPTIONS_PROMPT: str = "Please choose an option (1-3): "
DATA_OPTIONS: tuple[str, str, str] = (
    "Enter a new airport",
    "Fetch airport information",
    "Quit",
)
VALUE_ERROR_MSG: str = "Invalid option."
GOODBYE_MSG: str = "Thank you for using the Airport Data Management system. Goodbye!"


# Functions
def add_aiport(icao: str, name: str):
    """
    Adds new airport to airports dictionary.

    Args:
        icao (str): ICAO code of the airport. (key)
        name (str): Name of the airport. (value)
    """
    airports[icao] = name
    print(f"Airport {name} with ICAO code {icao} has been added.")


def get_airport_by_icao(icao: str) -> str:
    """
    Fetches airport from airports dictionary by `icao` key.

    Args:
        icao (str): ICAO code of the airport.
    Returns:
        str: Airport info or not found message.
    """
    if icao in airports.keys():
        return f"The airport with ICAO code {icao} is {airports[icao]}."
    else:
        return f"No airport found with ICAO code {icao}."


def manage_airport_data():
    """
    Keeps prompting the user for data management options.
    Option 3 quits the prompting.
    """
    while True:
        print(PROMPT_HEADING)
        for idx, option in enumerate(DATA_OPTIONS):
            print(f"{idx + 1}. {option}")
        while True:
            try:
                option_number = int(input(OPTIONS_PROMPT))
                if not 1 <= option_number <= len(DATA_OPTIONS):
                    raise ValueError
                break
            except ValueError:
                print(VALUE_ERROR_MSG)

        if option_number == 1:
            airport_code_and_name: list[str] = ["", ""]
            for idx, prompt in enumerate(AIRPORT_DATA_PROMPTS):
                airport_code_and_name[idx] = input(prompt)
            add_aiport(*airport_code_and_name)
        elif option_number == 2:
            airport_icao = input(AIRPORT_DATA_PROMPTS[0])
            print(get_airport_by_icao(airport_icao))
        elif option_number == 3:
            print(GOODBYE_MSG)
            break


# Variables
airports = dict()

# Main program.
manage_airport_data()
