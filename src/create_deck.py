

import re
from src import extract_units as eu
from src import get_pages as pg
from utils import ui_create_deck as ucd
from utils import ui_helpers as uh


def create_deck():
    units_data = eu.get_units_data()
    pages_data = pg.get_pages_data(units_data)
    total_pages = len(pages_data)
    page = 0
    deck = []
    show_help = False
    while True:
        page_ui = ucd.convert_page_ui(ui_data=pages_data, idx=page, deck=deck, show_help=show_help)
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
            if unit_code := re.search(r"^([0-9]{1,3})-([a-c])$", chosen):
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