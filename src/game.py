

import sys
from src import create_deck as cd
from src import menus as mn
from utils import ui


def main_menu():
    ui.show_title()
    main_menu_data = mn.get_main_menu()
    main_menu_ui = ui.convert_data_ui_menu(main_menu_data)

    while True:
        ui.display(main_menu_ui)
        chosen = input("                 >>> ")
        if chosen in main_menu_data["options"]:
            route = {
            "a": player_menu,
            "b": lambda: print("To be implemented."),
            "c": sys.exit
            }
            route[chosen]()


def player_menu():
    player_menu_data = mn.get_player_menu()
    player_menu_ui = ui.convert_data_ui_menu(player_menu_data)

    while True:
        ui.display(player_menu_ui)
        chosen = input("                 >>> ")
        if chosen in player_menu_data["options"]:
            route = {
            "a": create_deck_ui,
            "b": lambda: print("To be implemented."),
            "c": lambda: True
            }
            if route[chosen]():
                break


def create_deck_ui():
    ui_data = cd.get_create_deck()
    menu_data = ui.convert_data_ui_player(ui_data)
    ui.display(menu_data)