

import sys
from src import deck_creation_logic as dc
from src import get_menus as gm
from ui import menu as mn
from ui import prompt as pr
from ui import title as tt
from utils import ui_helpers as uh


def main_menu():
    tt.show_title()

    menu_data = gm.get_main_menu()
    menu_ui = mn.convert_menu_ui(menu_data)
    while True:
        uh.display(menu_ui)
        chosen = input("                 >>> ").strip()
        if chosen in menu_data["options"]:
            route = {
            "a": player_decks,
            "b": lambda: print("To be implemented."),
            "c": sys.exit
            }
            route[chosen]()


def player_decks():
    if not (deck_1 := player_menu(1)):
        return
    if not (deck_2 := player_menu(2)):
        return
    battle(deck_1, deck_2)


def player_menu(player_number):
    menu_data = gm.get_player_menu(player_number)
    menu_ui = mn.convert_menu_ui(menu_data)
    while True:
        uh.display(menu_ui)
        chosen = input("                 >>> ").strip()
        if chosen in menu_data["options"]:
            route = {
            "a": dc.deck_creation_logic,
            "b": lambda: print("To be implemented."),
            "c": lambda: "Back"
            }
            result = route[chosen]()
            if result == "Back":
                return
            elif result:
                return result


def battle(deck_1, deck_2):
    starting_battle_ui = pr.prompt("Starting battle...")
    uh.display(starting_battle_ui)
    input("                ")