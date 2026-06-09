

import sys
from src import menus as mn
from utils import ui


def main_menu():
    ui.show_title()
    input()
    menu_data = mn.get_main_menu()
    menu_ui = ui.convert_data_ui(menu_data)

    while True:
        ui.display(menu_ui)
        chosen = input("                 >>> ")
        if chosen in menu_data["options"]:
            route = {
            "a": player_menu,
            "b": lambda: print("To be implemented."),
            "c": sys.exit
            }
            route[chosen]()


def player_menu():
    player_menu_data = mn.get_play_menu()
    player_menu_ui = ui.convert_data_ui(player_menu_data)

    while True:
        ui.display(player_menu_ui)
        chosen = input("                 >>> ")
        if chosen in player_menu_data["options"]:
            route = {
            "a": lambda: print("To be implemented."),
            "b": lambda: print("To be implemented."),
            "c": lambda: True
            }
            if route[chosen]():
                break