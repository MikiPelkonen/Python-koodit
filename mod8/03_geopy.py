import mysql.connector
from mysql.connector import Error
from typing import Optional
from geopy import distance

# Constants.
CONFIG: dict = {
    "host": "127.0.0.1",
    "port": 3306,
    "database": "flight_game",
    "user": "smol",
    "password": "2122",
    "autocommit": True,
}
DB_CONN_ERR_PREFIX: str = "Database connection error: "
CALC_ERROR_MSG: str = "Error calculation distance between airports."


# Classes.
class Airport:
    """Represents an airport with ICAO code and (latitude, longitude) coords."""

    def __init__(self, icao: str, lat: float, lon: float) -> None:
        self.icao = icao
        self.coords = (lat, lon)

    def __repr__(self) -> str:
        return f"Airport ICAO: {self.icao} Latitude: {self.coords[0]:.2f} Longitude: {self.coords[1]:.2f}"


# Functions.
def get_airport_coordinates(icao_code: str) -> Optional[Airport]:
    """
    Fetches an airport coordinate info from database by given ICAO code.

    Args:
        icao_code (str): ICAO code of the airport.

    Returns:
        Airport: ICAO code and coordinates.
    """
    try:
        with mysql.connector.connect(**CONFIG) as connection:
            icao_to_upper = icao_code.upper()
            sql = "SELECT `latitude_deg`, `longitude_deg` FROM `airport` WHERE `ident` = %s"
            with connection.cursor(dictionary=True) as cursor:
                cursor.execute(sql, (icao_to_upper,))
                row = cursor.fetchone()
                if row:
                    airport = Airport(
                        icao_to_upper,
                        row["latitude_deg"],  # type: ignore
                        row["longitude_deg"],  # type: ignore
                    )
                    print(airport)
                    return airport
                else:
                    print(f"Airport with ICAO code: {icao_to_upper} not found.")
                    return None

    except Error as err:
        print(DB_CONN_ERR_PREFIX, err)
        return None


def run_airport_distance():
    """Prompts user for two airport ICAO codes and calculates the distance in kilometers between the given airports."""
    airport_list = []
    for i in range(2):
        airport_list.append(
            get_airport_coordinates(
                input(
                    f"Enter the ICAO code of the {'first' if i == 0 else 'second'} airport: "
                )
            )
        )

    if airport_list[0] is not None and airport_list[1] is not None:
        distance_in_kms = distance.great_circle(
            (airport_list[0].coords),
            (airport_list[1].coords),
        ).km

        print(
            f"The distance between {airport_list[0].icao} and {airport_list[1].icao}: {distance_in_kms:.2f} kilometers"
        )
    else:
        print(CALC_ERROR_MSG)


# Main program.
run_airport_distance()
