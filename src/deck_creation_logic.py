

import re
from src import get_menus as gm
from src import get_pages as gp
from ui import deck_creation as cd
from ui import menu as mn
from ui import prompt as pr
from utils import access_json as aj
from utils import ui_helpers as uh


def deck_creation_logic():
    units_data = aj.load_json_data("units_default.json")
    pages_data = gp.get_pages_data(units_data)
    deck = deck_creator(pages_data)
    if not deck:
        return

    menu_data = gm.get_save_deck_menu()
    menu_ui = mn.convert_menu_ui(menu_data)

    while True:
        uh.display(menu_ui)
        chosen = input("                 >>> ").strip()
        if chosen in menu_data["options"]:
            if chosen == "a":
                save_deck(deck)
                break
            break

    return deck


def deck_creator(pages_data):
    total_pages = len(pages_data)
    page = 0
    deck = []
    show_help = False
    while True:
        page_ui = cd.convert_page_ui(ui_data=pages_data, idx=page, deck=deck, show_help=show_help)
        uh.display(page_ui)
        chosen = input("    >>> ").strip().lower()

        visible_page = page + 1
        show_help = False

        if not chosen:
            continue

        if chosen == "h":
            show_help = True

        if chosen == "e" and visible_page > 1:
            page -= 1
        if chosen == "r" and visible_page < total_pages:
            page += 1

        if page_number := re.search(r"^([0-9]{1,3})$", chosen):
            selected_page = int(page_number.group(1)) - 1
            if 0 <= selected_page < total_pages:
                page = selected_page

        if len(deck) <= 2:
            if unit_code := re.search(r"^([0-9]{1,3})([a-c])$", chosen):
                unit_number = int(unit_code.group(1)) - 1
                unit_trait = unit_code.group(2)
                options = {
                    "a": "T1",
                    "b": "T2",
                    "c": "T3"
                }
                deck.append(f"{options[unit_trait]}-{pages_data[unit_number]["name"].title()}")

        if chosen == "d" and bool(deck):
            del deck[-1]

        if chosen == "b":
            return

        if chosen == "f" and len(deck) == 3:
            return deck


def save_deck(deck):
    decks_data = aj.load_json_data("saved_decks.json")
    prompt_name_ui = pr.prompt("Enter a name for your deck")
    while True:
        uh.display(prompt_name_ui)
        deck_name = input("                 >>> ").strip()
        if deck_name:
            decks_data.append({
                "name": deck_name,
                "slots": deck
            })
            aj.dump_json_data("saved_decks.json", decks_data)
            break