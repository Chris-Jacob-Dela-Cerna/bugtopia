

import sys


def get_main_menu():
    from src.game import player_menu
    return {
        "header": "Main Menu",
        "options": {
            "a": "Play 1v1",
            "b": "Credits",
            "c": "Quit"
        },
        "route": {
            "a": player_menu,
            "b": lambda: print("To be implemented."),
            "c": sys.exit
        }
    }


def get_play_menu():
    return {
        "header": "Player 1",
        "options": {
            "a": "Create a Deck",
            "b": "Select an Existing Deck",
            "c": "Back"
        },
        "route": {
            "a": lambda: print("To be implemented."),
            "b": lambda: print("To be implemented."),
            "c": lambda: True
        }
    }