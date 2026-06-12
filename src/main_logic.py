

import sys
from src import create_deck as cd
from src import get_menus as gm
from ui import menu as mn
from ui import title as tt
from utils import ui_helpers as uh


def main_menu():
    tt.show_title()
    main_menu_data = gm.get_main_menu()
    main_menu_ui = mn.convert_data_ui_menu(main_menu_data)

    while True:
        uh.display(main_menu_ui)
        chosen = input("                 >>> ").strip()
        if chosen in main_menu_data["options"]:
            route = {
            "a": player_deck_creation,
            "b": lambda: print("To be implemented."),
            "c": sys.exit
            }
            route[chosen]()


def player_deck_creation():
    if not (deck_1 := player_menu(1)):
        return
    if not (deck_2 := player_menu(2)):
        return


def player_menu(player_number):
    player_menu_data = gm.get_player_menu(player_number)
    player_menu_ui = mn.convert_data_ui_menu(player_menu_data)

    while True:
        uh.display(player_menu_ui)
        chosen = input("                 >>> ").strip()
        if chosen in player_menu_data["options"]:
            route = {
            "a": cd.create_deck,
            "b": lambda: print("To be implemented."),
            "c": lambda: "Back"
            }
            result = route[chosen]()
            if result == "Back":
                return
            elif result:
                return result