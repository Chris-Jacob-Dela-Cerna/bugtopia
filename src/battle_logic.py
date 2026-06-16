

from src import get_unit_idx as gu
from src import unit_class as uc
from ui import battle_screen as bs
from utils import access_json as aj
from utils import ui_helpers as uh


def battle_logic(deck_1, deck_2):
    units_data = aj.load_json_data("units_default.json")
    player_1 = convert_player_deck(deck_1, units_data)
    player_2 = convert_player_deck(deck_2, units_data)

    while True:
        control_panel_data = get_control_panel_data([player_1, player_2])
        battle_ui = bs.convert_battle_ui(player_1, player_2, control_panel_data)
        uh.display(battle_ui)
        input("    >>> ").strip().lower()


def convert_player_deck(deck, units_data):
    deck_units_idx = [gu.get_unit_idx(unit_slot, units_data) for unit_slot in deck]
    return [uc.Unit(units_data, *unit_idx) for unit_idx in deck_units_idx]


def get_control_panel_data(player, current_player=0, panel_mode=0):
    control_panel_data = {'options': [""]}
    if panel_mode == 0:
        control_panel_data['header'] = "Select a unit:"
    elif panel_mode == 1:
        control_panel_data['header'] = "Choose an ability:"
    elif panel_mode == 2:
        control_panel_data['header'] = "Inflict on:"

    return control_panel_data




control_panel_data_example = {
    "header": "Select a unit:",
    "options": [
        "a. Fire Ant (100 HP)",
        "b. Hercules Beetle (200 HP)",
        "",
        "",
        "e. Back"
    ]
}