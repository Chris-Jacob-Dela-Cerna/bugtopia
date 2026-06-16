

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
        control_panel_data = get_control_panel_data(player_1, player_2)
        battle_ui = bs.convert_battle_ui(player_1, player_2, control_panel_data)
        uh.display(battle_ui)
        input("    >>> ").strip().lower()


def convert_player_deck(deck, units_data):
    deck_units_idx = [gu.get_unit_idx(unit_slot, units_data) for unit_slot in deck]
    return [uc.Unit(units_data, *unit_idx) for unit_idx in deck_units_idx]


def get_control_panel_data(current_player, enemy_player, panel_mode=2):
    control_panel_data = {}
    letters = "abcde"
    options = []

    if panel_mode == 0:
        header = "Select a unit:"
        options.extend([f"{letters[x]}. {unit.trait} {unit.unit} ({unit.health} HP)" for x, unit in enumerate(current_player)])
        unit_count = len(current_player)
        if unit_count < 4:
            options.extend(["" for _ in range(4 - unit_count)])
        options.append("e. Skip")

    elif panel_mode == 1:
        header = "Choose an ability:"

    elif panel_mode == 2:
        header = "Inflict on:"
        options.extend([f"{letters[x]}. {unit.trait} {unit.unit} ({unit.health} HP)" for x, unit in enumerate(enemy_player)])
        unit_count = len(enemy_player)
        if unit_count < 4:
            options.extend(["" for _ in range(4 - unit_count)])
        options.append("e. Back")

    control_panel_data['header'] = header
    control_panel_data['options'] = options

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