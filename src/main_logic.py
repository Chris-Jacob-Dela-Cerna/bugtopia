

import sys
from src import create_deck as cd
from src import get_menus as mn
from utils import ui
from utils import ui_helpers as uh
from utils import ui_menu as um


def main_menu():
    ui.show_title()
    main_menu_data = mn.get_main_menu()
    main_menu_ui = um.convert_data_ui_menu(main_menu_data)

    while True:
        uh.display(main_menu_ui)
        chosen = input("                 >>> ").strip()
        if chosen in main_menu_data["options"]:
            route = {
            "a": player_menu,
            "b": lambda: print("To be implemented."),
            "c": sys.exit
            }
            route[chosen]()


def player_menu():
    player_menu_data = mn.get_player_menu()
    player_menu_ui = um.convert_data_ui_menu(player_menu_data)

    while True:
        uh.display(player_menu_ui)
        chosen = input("                 >>> ").strip()
        if chosen in player_menu_data["options"]:
            route = {
            "a": cd.create_deck,
            "b": lambda: print("To be implemented."),
            "c": lambda: True
            }
            if route[chosen]():
                break