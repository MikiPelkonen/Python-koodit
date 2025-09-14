import mysql.connector
from mysql.connector import Error

# Constants.
COUNTRY_PROMPT: str = "Enter the country code (e.g., FI for Finland): "
CONFIG = {
    "host": "127.0.0.1",
    "port": 3306,
    "database": "flight_game",
    "user": "smol",
    "password": "2122",
    "autocommit": True,
}


# Functions.
def get_airports_by_country_code(country_code: str) -> dict[str, list[str]]:
    """
    Fetch airports by country code from database.

    Returns:
        dict[str, list[str]: A dictionary where keys are airport types and values list of airport names.
    """
    try:
        with mysql.connector.connect(**CONFIG) as connection:
            country_code_upper = country_code.upper()
            sql = "SELECT * FROM `airport` WHERE `iso_country` = %s"

            with connection.cursor(dictionary=True) as cursor:
                cursor.execute(sql, (country_code_upper,))
                rows = cursor.fetchall()
                airports_by_type = {}

                for airport in rows:
                    airport_type = airport["type"]  # type: ignore
                    airports_by_type.setdefault(airport_type, []).append(
                        airport["name"]  # type: ignore
                    )

                return airports_by_type

    except Error as err:
        print(f"Database connection error: {err}")
        return {}


def run_country_program():
    """Prompts user for country code and lists all airports from the given country."""
    user_input = input(COUNTRY_PROMPT)
    airports = get_airports_by_country_code(user_input)
    if airports:
        print(f"\nAirports in {user_input}: ")
        for airport_type, names in airports.items():
            print(f"{airport_type} ({len(names)}): ")
            for name in names:
                print(f" - {name}")
    else:
        print(f"No airports found with country code: {user_input}")


# Main program.
run_country_program()
