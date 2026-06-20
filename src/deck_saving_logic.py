

from src import get_menus as gm
from ui import menu as mn
from ui import prompt as pr
from utils import access_json as aj
from utils import ui_helpers as uh


def deck_saving_logic(deck):
    menu_data = gm.get_save_deck_menu()
    menu_ui = mn.render_menu_ui(menu_data)
    while True:
        uh.display(menu_ui)
        chosen = input("                 >>> ").strip()
        if chosen in menu_data["options"]:
            if chosen == "a":
                save_deck(deck)
                break
            break


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
            starting_battle_ui = pr.prompt("Deck saved.")
            uh.display(starting_battle_ui)
            input("                ")
            break