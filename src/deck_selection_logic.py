

from ui import deck_selection as ds
from utils import access_json as aj
from utils import ui_helpers as uh


def deck_creation_logic():
    raw_decks_data = aj.load_json_data("saved_decks.json")
    decks_data = convert_decks_data(raw_decks_data)
    deck = deck_selector(decks_data)
    if not deck:
        return
    return deck


def deck_selector(decks_data):
    total_pages = len(decks_data)
    page = 0
    deck = []
    show_help = False
    while True:
        deck_ui = ds.render_deck_ui(decks_data, page, show_help)
        uh.display(deck_ui)
        chosen = input("    >>> ").strip().lower()


def convert_decks_data(raw_decks_data):
    ...