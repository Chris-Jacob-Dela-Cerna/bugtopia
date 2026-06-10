

import re
import sys
from src import extract_units as eu
from src import get_menus as mn
from src import get_pages as pg
from utils import ui
from utils import ui_create_deck as ucd
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
            "a": create_deck,
            "b": lambda: print("To be implemented."),
            "c": lambda: True
            }
            if route[chosen]():
                break


def create_deck():
    units_data = eu.get_units_data()
    pages_data = pg.get_pages_data(units_data)
    total_pages = len(pages_data)
    page = 0
    show_help = False
    while True:
        page_ui = ucd.convert_page_ui(pages_data, page, ["T1-Warrior", "T3-Archer"], show_help)
        uh.display(page_ui)
        chosen = input("    >>> ").strip().lower()
        if not chosen:
            continue
        show_help = False
        if chosen == "help":
            show_help = True

        if chosen == "e" and page > 0:
            page -= 1
        if chosen == "r" and page < total_pages - 1:
            page += 1

        if page_number := re.search(r"^([0-9]{1,3})$", chosen):
            page_idx = int(page_number.group(1)) - 1
            if 0 <= page_idx < total_pages:
                page = page_idx

        if re.search(r"^([0-9]{1,3})-([a-c])$", chosen):
            print("Unit-Trait")
        if chosen == "bb":
            print("Undo")