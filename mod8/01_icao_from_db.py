import mysql.connector
from mysql.connector import Error

# Constants.
ICAO_PROMPT: str = "Enter the ICAO code of an airport: "
CONFIG = {
    "host": "127.0.0.1",
    "port": 3306,
    "database": "flight_game",
    "user": "smol",
    "password": "2122",
    "autocommit": True,
}


# Functions.
def get_airport_by_icao_code(icao_code: str):
    """Fetch airport name and location by ICAO code from database."""
    try:
        with mysql.connector.connect(**CONFIG) as connection:
            icao_upper = icao_code.upper()
            sql = "SELECT `name` as `Airport name`, `municipality` AS `Location` FROM `airport` WHERE `ident` = %s"

            with connection.cursor() as cursor:
                cursor.execute(sql, (icao_upper,))
                row = cursor.fetchone()

                if row is None:
                    print(f"No airport found with ICAO code: {icao_upper}")
                else:
                    print(f"Airport name: {row[0]}\nLocation: {row[1]}")  # type: ignore

                return row

    except Error as err:
        print(f"Database connection error: {err}")


# Main program.
user_input = input(ICAO_PROMPT)
get_airport_by_icao_code(user_input)
