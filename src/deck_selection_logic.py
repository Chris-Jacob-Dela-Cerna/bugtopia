

from src import deck_creation_logic as dcl
from ui import deck_selection as ds
from utils import access_json as aj
from utils import ui_helpers as uh


def deck_creation_logic():
    raw_decks_data = aj.load_json_data("saved_decks.json")
    if not raw_decks_data:
        return
    decks_data = convert_decks_data(raw_decks_data)
    deck = deck_selector(decks_data)
    if not deck:
        return
    return deck


def deck_selector(raw_decks_data, decks_data):
    total_pages = len(raw_decks_data)
    page = 0
    show_help = False
    while True:
        deck_ui = ds.render_deck_ui(decks_data, page, show_help)
        uh.display(deck_ui)
        chosen = input("    >>> ").strip().lower()

        visible_page = page + 1
        show_help = False
        if not chosen:
            continue

        if chosen == "h":
            show_help = True
        if chosen == "b":
            return
        if chosen == "f":
            return raw_decks_data[page]['deck']

        page = dcl.handle_page(chosen, page, visible_page, total_pages)


def convert_decks_data(raw_decks_data):
    ...