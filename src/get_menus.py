

def get_main_menu():
    return {
        "header": "Main Menu",
        "options": {
            "a": "Play 1v1",
            "b": "Credits",
            "c": "Quit"
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