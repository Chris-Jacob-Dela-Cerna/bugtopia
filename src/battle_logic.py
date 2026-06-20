

from src import battle_panel_logic as bpl
from src import get_bug_idx as gb
from src import bug_state_logic as bsl
from src import bug_class as bc
from ui import battle_screen as bs
from utils import access_json as aj
from utils import ui_helpers as uh


def battle_logic(deck_1, deck_2):
    bugs_data = aj.load_json_data("bugs_data.json")
    player_1 = convert_player_deck(deck_1, bugs_data)
    player_2 = convert_player_deck(deck_2, bugs_data)
    players = [player_1, player_2]
    turns = 0
    while True:
        turns += 1
        bsl.run_per_turn_checks(players)
        player_turn_logic(player_1, player_2, turns)

        bsl.run_per_instance_checks(players)
        player_turn_logic(player_2, player_1, turns)


def player_turn_logic(attacker, defender, turns):
    panel_mode = 0
    selected_bug = None
    selected_ability = None
    selected_target = None

    while True:
        if panel_mode == 0:
            panel, options = bpl.selection_panel(attacker)
            chosen = load_battle_ui(attacker, defender, panel, turns)
            if chosen in options:
                selected_bug = options[chosen]
                panel_mode = 1
                continue
            elif chosen == "e":
                break

        elif panel_mode == 1:
            panel, options = bpl.ability_panel(selected_bug)
            chosen = load_battle_ui(attacker, defender, panel, turns)
            if chosen in options:
                selected_ability = options[chosen]
                if bsl.check_self_ability(selected_bug, selected_ability):
                    break
                else:
                    panel_mode = 2
                    continue
            elif chosen == "e":
                panel_mode = 0
                continue

        elif panel_mode == 2:
            panel, options = bpl.attack_panel(defender, selected_ability)
            chosen = load_battle_ui(attacker, defender, panel, turns)
            if chosen in options:
                selected_target = options[chosen]
                if bsl.check_inflicting_ability(selected_bug, selected_ability, selected_target):
                    break
                else:
                    continue
            elif chosen == "e":
                panel_mode = 1
                continue


def convert_player_deck(deck, bugs_data):
    deck_bugs_idx = [gb.get_bug_idx(bug_slot, bugs_data) for bug_slot in deck]
    return [bc.Bug(bugs_data, *bug_idx) for bug_idx in deck_bugs_idx]


def load_battle_ui(attacker, defender, panel, turns):
    battle_ui = bs.convert_battle_ui(attacker, defender, panel, turns)
    uh.display(battle_ui)
    return input("    >>> ").strip().lower()