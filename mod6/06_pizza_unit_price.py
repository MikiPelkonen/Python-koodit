"""
File: 06_pizza_unit_price.py

Description:
    Prompts user for diameter and price of 2 pizzas.
    Calculates and prints the unit prices in euros per square meter.
    Determines which pizza offers better value for money.

Classes:
    Pizza(NamedTuple):
        Represents a pizza with a diameter, price and unit_price property.

Functions:
    calculate_unit_price(diameter: float, price: float) -> float:
        Returns unit price in euro per m².
    prompt_for_pizza_data(key: str) -> Pizza:
        Prompts user for pizza data and returns new pizza object.
    compare_pizzas(pizza_dict: dict[str, Pizza]) -> None:
        Compares pizzas in dictionary and prints one with the best value for money.

Author: Miki Pelkonen
Date: 2025-08-29
"""

# Imports.
from math import pi, isclose
from typing import NamedTuple


# Classes.
class Pizza(NamedTuple):
    """
    Represents a pizza.

    Attributes:
        diameter (float): Diameter of the pizza in centimeters.
        price (float): Total price in euros.
        unit_price (float): The calculated price per square meter in euros. (Read-only property).
    """

    diameter: float
    price: float

    @property
    def unit_price(self) -> float:
        """Get unit price in euros pre square meter."""
        return calculate_unit_price(*self)

    def formatted_unit_price(self, key: str) -> str:
        """
        Returns a formatted string showing the pizza's unit price.

        Args:
            key (str): Label for the pizza (e.g. "first", "second").

        Returns:
            str: Formatted string including key identifier and unit price in euros per square meter.
        """
        return f"Unit price of the {key} pizza: {self.unit_price:.2f} euros/m²"


# Constants.
INVALID_INPUT_MSG: str = "Please enter a valid number."
PIZZA_KEYS: tuple[str, str] = "first", "second"
PIZZA_DICT: dict[str, Pizza] = {}


# Functions.
def calculate_unit_price(diameter: float, price: float) -> float:
    """
    Calculates unit price from `diameter` and `price`.

    Args:
        diameter (float): Diameter of a circle.
        price (float): Total price of the item in euros.

    Returns:
        float: Price per square meter in euros.
    """
    diameter_in_meters = diameter / 100
    area_in_m2 = pi * (diameter_in_meters**2) / 4
    unit_price = price / area_in_m2
    return unit_price


def prompt_for_pizza_data(key: str) -> Pizza:
    """
    Prompts user for diameter and price and returns new pizza object.

    Args:
        key (str): Identifier key. (e.g. "first", "second").

    Returns:
        Pizza: new Pizza object with diameter and price.
    """
    results = []
    for field in Pizza._fields:
        while True:
            try:
                prompt_unit = "cm" if field == "diameter" else "euros"
                results.append(
                    float(
                        input(f"Enter the {field} of the {key} pizza ({prompt_unit}): ")
                    )
                )
                break
            except ValueError:
                print(INVALID_INPUT_MSG)

    return Pizza(*results)


def compare_pizzas(pizza_dict: dict[str, Pizza]):
    """
    Compares pizzas in a dictionary and determines which is the best value for money.

    Args:
        pizza_dict (dict[str, Pizza]): Dictionary of pizzas to compare.
    """
    if all(
        isclose(pizza_dict[PIZZA_KEYS[0]].unit_price, p.unit_price, rel_tol=1e-9)
        for k, p in pizza_dict.items()
        if k != PIZZA_KEYS[0]
    ):
        print("The pizzas have equal unit price.")
        return

    lowest_unit_price: float = float("inf")
    best_pizza_key: str = ""

    for key, pizza in PIZZA_DICT.items():
        if pizza.unit_price < lowest_unit_price:
            lowest_unit_price = pizza.unit_price
            best_pizza_key = key

    print(f"The {best_pizza_key} pizza provides better value for money.")


# Main program.
for key in PIZZA_KEYS:
    PIZZA_DICT[key] = prompt_for_pizza_data(key)

for key, pizza in PIZZA_DICT.items():
    print(pizza.formatted_unit_price(key))

compare_pizzas(PIZZA_DICT)
