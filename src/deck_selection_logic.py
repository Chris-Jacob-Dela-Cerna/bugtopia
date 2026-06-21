

from src import deck_creation_logic as dcl
from src import get_bug_idx as gb
from ui import deck_selection as ds
from ui import prompt as pr
from utils import access_json as aj
from utils import ui_helpers as uh


def deck_selection_logic():
    raw_decks_data = aj.load_json_data("saved_decks.json")
    if not raw_decks_data:
        message = pr.prompt("No decks currently saved...")
        uh.display(message)
        input("                 ")
        return
    decks_data = convert_decks_data(raw_decks_data)
    deck = deck_selector(raw_decks_data, decks_data)
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
        chosen = input("             >>> ").strip().lower()

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
    bugs_data = aj.load_json_data("bugs_data.json")
    decks_data = []
    for saved_deck in raw_decks_data:
        saved_deck_data = {
            "name": saved_deck['name'], 
            "deck": []
        }
        for bug_slot in saved_deck['deck']:
            family_idx, species_idx = gb.get_bug_idx(bug_slot, bugs_data)
            bug = bugs_data[family_idx]
            saved_deck_data['deck'].append(f"{bug['species'][species_idx]['name'].title()} {bug['name'].title()}")
        decks_data.append(saved_deck_data)
    return decks_data