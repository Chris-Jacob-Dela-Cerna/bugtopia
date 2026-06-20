

import re
from src import deck_saving_logic as ds
from src import get_pages as gp
from ui import deck_creation as cd
from utils import access_json as aj
from utils import ui_helpers as uh


def deck_creation_logic():
    bugs_data = aj.load_json_data("bugs_data.json")
    pages_data = gp.get_pages_data(bugs_data)
    deck = deck_creator(pages_data)
    if not deck:
        return
    ds.deck_saving_logic(deck)
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
        if chosen == "b":
            return
        if chosen == "f" and len(deck) == 3:
            return deck
        
        page = handle_page(chosen, page, visible_page, total_pages)
        deck = handle_deck(chosen, deck, pages_data)


def handle_page(chosen, page, visible_page, total_pages):
    if chosen == "e" and visible_page > 1:
        page -= 1
    if chosen == "r" and visible_page < total_pages:
        page += 1
    if page_number := re.search(r"^([0-9]{1,3})$", chosen):
        selected_page = int(page_number.group(1)) - 1
        if 0 <= selected_page < total_pages:
            page = selected_page
    return page


def handle_deck(chosen, deck, pages_data):
    if len(deck) <= 2:
        if bug_id := re.search(r"^([0-9]{1,3})([a-c])$", chosen):
            bug_idx = int(bug_id.group(1)) - 1
            bug_family = bug_id.group(2)
            options = {
                "a": "T1",
                "b": "T2",
                "c": "T3"
            }
            deck.append(f"{options[bug_family]}-{pages_data[bug_idx]["name"].title()}")
    if chosen == "d" and deck:
        del deck[-1]
    return deck