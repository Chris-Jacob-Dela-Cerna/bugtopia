

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
            menu_data["route"][chosen]()


def player_menu():
    player_menu_data = mn.get_play_menu()
    player_menu_ui = ui.convert_data_ui(player_menu_data)

    while True:
        ui.display(player_menu_ui)
        chosen = input("                 >>> ")
        if chosen in player_menu_data["options"]:
            if player_menu_data["route"][chosen]():
                break