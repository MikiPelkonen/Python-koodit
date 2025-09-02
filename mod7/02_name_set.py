"""
File: 02_name_set.py

Description:
    A simple program that keeps prompting user for names and collects them in a set.
    Prints "New name" on unique keys and "Existing name" ond duplicate keys.
    Inputting empty string stops prompting and prints the results.

Functions:
    prompt_names_for_set() -> set[str]:

Example:
    >>> Enter a name: miki
    New name
    >>> Enter a name: miki
    Existing name
    >>> Enter a name:
    miki

Author: Miki Pelkonen
Date: 2025-09-02
"""

# Constants.
NAME_PROMPT: str = "Enter a name: "
NAME_RESULTS: tuple[str, str] = ("New name", "Existing name")


# Functions.
def prompt_names_for_set() -> set[str]:
    """
    Keeps prompting user for names until an empty string is passed.

    Returns:
        set[str]: The names in a set.
    """
    result_set: set[str] = set()
    while True:
        user_input = input(NAME_PROMPT)
        if not user_input:
            break
        try:
            if user_input in result_set:
                raise KeyError
            result_set.add(user_input)
            print(NAME_RESULTS[0])
        except KeyError:
            print(NAME_RESULTS[1])

    return result_set


# Main program.
names = prompt_names_for_set()
for name in names:
    print(name)
