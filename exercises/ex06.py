"""EX06 Dictionary Functions."""

__author__ = "730481331"


def invert(invert_dictionary: dict[str, str]) -> dict[str, str]:
    """When give a dictionary, a new dictionary will be produced except the keys and values from the first dictionary will be inverted on the second dictionary."""
    outcome: dict[str, str] = dict()
    for key in invert_dictionary:
        if invert_dictionary[key] in outcome:
            raise KeyError()
        outcome[invert_dictionary[key]] = key
    return outcome


def favorite_color(favorite_color_dictionary: dict[str, str]) -> str:
    """When given a dictionary of favorite colors, a sting will print with the color in the dictionary that is listed the most."""
    i: dict[str, int] = dict()
    outcome: str = ""
    for key in favorite_color_dictionary:
        if outcome == "":
            outcome = favorite_color_dictionary[key]
        if not favorite_color_dictionary[key] in i:
            i[favorite_color_dictionary[key]] = 1
        else:
            i[favorite_color_dictionary[key]] += 1
    for key in i:
        if i[key] > i[outcome]:
            outcome = key
    return outcome


def count(list[str]) -> [dict[str, int]]:
    """When given a list of stings, the dictionary will reflect the number of times the string was lited in the list. """
    dictionary: dict[str, int]
    dictionary = dict()
    i = 0
    times: int = 1
    while i <= len(list):
        for list[i] in list[str]:
            list[i] = dictionary[list[i]] = times
        if list[i] in dictionary:
            dictionary[list[i]] = times + 1
        i += 1
    return dictionary 