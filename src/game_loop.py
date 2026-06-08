

from src import menus as mn
from utils import ui


def main_loop():
    ui.show_title()
    menu_data = mn.get_main_menu()
    menu_ui = ui.convert_data_ui(menu_data)

    while True:
        ui.display(menu_ui)
        chosen = input("                 >>> ")

        if chosen in menu_data["options"]:
            while True:
                if menu_data["route"][chosen]():
                    break