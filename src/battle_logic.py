

from src import get_unit_idx as gu
from src import unit_class as uc
from ui import battle_screen as bs
from utils import access_json as aj
from utils import ui_helpers as uh


def battle_logic(deck_1, deck_2):
    units_data = aj.load_json_data("units_default.json")
    player_1 = convert_player_deck(deck_1, units_data)
    player_2 = convert_player_deck(deck_2, units_data)
    panel_mode = 2
    selected_unit = None

    while True:
        control_panel_data = get_control_panel_data(player_1, player_2, panel_mode, selected_unit)
        battle_ui = bs.convert_battle_ui(player_1, player_2, control_panel_data)
        uh.display(battle_ui)
        chosen = input("    >>> ").strip().lower()


def convert_player_deck(deck, units_data):
    deck_units_idx = [gu.get_unit_idx(unit_slot, units_data) for unit_slot in deck]
    return [uc.Unit(units_data, *unit_idx) for unit_idx in deck_units_idx]


def get_control_panel_data(current_player, enemy_player, panel_mode=0, selected_unit=None):
    letters = "abcde"
    if panel_mode == 0:
        header = "Select a unit:"
        options = [f"{letters[x]}. {unit.trait} {unit.unit} ({unit.health} HP)" for x, unit in enumerate(current_player)]
        footer = "e. Skip"
    elif panel_mode == 1:
        header = "Choose an ability:"
        options = [f"{letters[x]}. {ability}" for x, ability in enumerate(selected_unit.abilities)]
        footer = "e. Back"
    elif panel_mode == 2:
        header = "Inflict on:"
        options = [f"{letters[x]}. {unit.trait} {unit.unit} ({unit.health} HP)" for x, unit in enumerate(enemy_player)]
        footer = "e. Back"
    else:
        raise ValueError("Invalid panel mode.")
    return contruct_panel(header, options, footer)


def contruct_panel(header, options, footer):
    if len(options) < 4:
        options.extend(["" for _ in range(4 - len(options))])
    options.append(footer)
    return {
        "header": header,
        "options": options
    }