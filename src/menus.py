

from src.game import player_menu


def get_main_menu():
    return {
        "header": "Main Menu",
        "options": {
            "a": "Play 1v1",
            "b": "Credits",
            "c": "Quit"
        }
    }


def get_play_menu():
    return {
        "header": "Player 1",
        "options": {
            "a": "Create a Deck",
            "b": "Select an Existing Deck",
            "c": "Back"
        }
    }