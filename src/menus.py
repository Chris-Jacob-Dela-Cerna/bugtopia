

import sys


def get_main_menu():
    return {
        "header": "Main Menu",
        "options": {
            "a": "Play 1v1",
            "b": "Credits",
            "c": "Quit"
        },
        "route": {
            "a": get_play_menu,
            "b": lambda: True,
            "c": sys.exit
        }
    }


def get_play_menu():
    return {
        "header": "Main Menu",
        "options": {
            "a": "Create a Deck",
            "b": "Select an Existing Deck",
            "c": "Back"
        },
        "route": {
            "a": lambda: True,
            "b": lambda: True,
            "c": lambda: True
        }
    }