

from src import battle_panel_logic as bpl
from src import get_unit_idx as gu
from src import unit_state_logic as usl
from src import unit_class as uc
from ui import battle_screen as bs
from ui import prompt as pr
from utils import access_json as aj
from utils import ui_helpers as uh


def battle_logic(deck_1, deck_2):
    units_data = aj.load_json_data("units_default.json")
    player_1 = convert_player_deck(deck_1, units_data)
    player_2 = convert_player_deck(deck_2, units_data)
    players = [player_1, player_2]
    turns = 0
    while True:
        turns += 1
        usl.run_per_turn_checks(players)
        usl.run_per_turn_checks(players)
        player_turn_logic(player_1, player_2, turns)

        usl.run_per_instance_checks(players)
        usl.run_per_instance_checks(players)
        player_turn_logic(player_2, player_1, turns)


def player_turn_logic(attacker, defender, turns):
    global panel_mode
    panel_mode = 0
    selected_unit = None
    selected_ability = None
    selected_target = None
    letters = "abcd"

    while True:
        if panel_mode == 0:
            panel, options = bpl.selection_panel(attacker)
            chosen = load_battle_ui(attacker, defender, panel, turns)
            if chosen in options:
                selected_unit = options[chosen]
                panel_mode = 1
                continue
            elif chosen == "e":
                break

        elif panel_mode == 1:
            panel, options = bpl.ability_panel(selected_unit)
            if chosen in options:
                selected_ability = options[chosen]
                if usl.check_self_ability(unit, selected_ability):
                    panel_mode = 0
                    break
                else:
                    panel_mode = 2
                    continue
            elif chosen == "e":
                panel_mode = 0
                continue

        elif panel_mode == 2:
            options = {}
            for x, unit in enumerate(defender):
                if unit:
                    if selected_ability not in unit.blocked_abilities:
                        options[letters[x]] = unit
            if chosen in options.keys():
                target = options[chosen]
                if usl.check_inflicting_ability(unit, selected_ability, target):
                    panel_mode = 0
                    break
                continue
            elif chosen == "e":
                panel_mode = 1
                continue


def convert_player_deck(deck, units_data):
    deck_units_idx = [gu.get_unit_idx(unit_slot, units_data) for unit_slot in deck]
    return [uc.Unit(units_data, *unit_idx) for unit_idx in deck_units_idx]


def load_battle_ui(attacker, defender, panel, turns):
    battle_ui = bs.convert_battle_ui(attacker, defender, panel, turns)
    uh.display(battle_ui)
    return input("    >>> ").strip().lower()