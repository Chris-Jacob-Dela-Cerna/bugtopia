

def get_main_menu():
    return {
        "header": "Main Menu",
        "options": {
            "a": "Play",
            "b": "Quit"
        }
    }


def get_player_menu(player_number):
    return {
        "header": f"Player {player_number}",
        "options": {
            "a": "Create a Deck",
            "b": "Select an Existing Deck",
            "c": "Back to Main Menu"
        }
    }


def get_save_deck_menu():
    return {
        "header": "Save deck?",
        "options": {
            "a": "Yes",
            "b": "No"
        }
    }