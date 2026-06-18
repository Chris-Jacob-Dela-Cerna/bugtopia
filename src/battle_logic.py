

from src import get_unit_idx as gu
from src import unit_class as uc
from ui import battle_screen as bs
from ui import prompt as pr
from utils import access_json as aj
from utils import ui_helpers as uh


def battle_logic(deck_1, deck_2):
    units_data = aj.load_json_data("units_default.json")
    player_1 = convert_player_deck(deck_1, units_data)
    player_2 = convert_player_deck(deck_2, units_data)
    turn = 1
    while True:
        uh.display(pr.prompt("Player 1"))
        input("                ")
        player_battle_turn(player_1, player_2, turn, 1)

        for x, unit in enumerate(player_1):
            if unit:
                unit.check_general_status()
                if not unit.is_alive:
                    player_1[x] = None
        for x, unit in enumerate(player_2):
            if unit:
                unit.check_general_status()
                if not unit.is_alive:
                    player_2[x] = None

        uh.display(pr.prompt("Player 2"))
        input("                ")
        player_battle_turn(player_2, player_1, turn, 2)

        for x, unit in enumerate(player_1):
            if unit:
                unit.check_general_status()
                unit.check_applied_status()
                if not unit.is_alive:
                    player_1[x] = None
        for x, unit in enumerate(player_2):
            if unit:
                unit.check_general_status()
                unit.check_applied_status()
                if not unit.is_alive:
                    player_2[x] = None
        turn += 1


def player_battle_turn(current_player, enemy_player, turn, player_turn):
    panel_mode = 0
    selected_unit = None
    selected_ability = None
    selected_target = None
    letters = "abcd"

    while True:
        control_panel_data = get_control_panel_data(current_player, enemy_player, panel_mode, selected_unit, selected_ability, selected_target)
        battle_ui = bs.convert_battle_ui(current_player, enemy_player, control_panel_data, turn, player_turn)
        uh.display(battle_ui)
        chosen = input("    >>> ").strip().lower()

        if panel_mode == 0:
            options = {letters[x]: unit for x, unit in enumerate(current_player) if unit}
            if chosen in options.keys():
                selected_unit = options[chosen]
                panel_mode = 1
                continue
            elif chosen == "e":
                break

        elif panel_mode == 1:
            options = {}
            overlap = 0
            for x, ability in enumerate(selected_unit.abilities):
                if ability and ability not in selected_unit.blocked_abilities:
                    options[letters[x - overlap]] = ability
                else:
                    overlap += 1
            if chosen in options.keys():
                selected_ability = options[chosen]
                if check_self_ability(selected_unit, selected_ability):
                    panel_mode = 0
                    break
                panel_mode = 2
                continue
            elif chosen == "e":
                panel_mode = 0
                continue

        elif panel_mode == 2:
            options = {}
            overlap = 0
            for x, unit in enumerate(enemy_player):
                if unit:
                    if selected_ability not in unit.blocked_abilities:
                        options[letters[x - overlap]] = unit
                    else:
                        overlap += 1
            if chosen in options.keys():
                selected_target = options[chosen]
                if check_inflicting_ability(selected_unit, selected_ability, selected_target):
                    panel_mode = 0
                    break
                continue
            elif chosen == "e":
                panel_mode = 1
                continue


def get_control_panel_data(current_player, enemy_player, panel_mode=0, selected_unit=None, selected_ability=None, selected_target=None):
    letters = "abcd"
    if panel_mode == 0:
        header = "Select a unit:"
        options = [f"{letters[x]}. {unit.trait} {unit.unit} ({unit.health} HP)" for x, unit in enumerate(current_player) if unit]
        footer = "e. Skip"
    elif panel_mode == 1:
        header = "Choose an ability:"
        options = []
        overlap = 0
        for x, ability in enumerate(selected_unit.abilities):
            if ability not in selected_unit.blocked_abilities:
                options.append(f"{letters[x - overlap]}. {ability}")
            else:
                overlap += 1
        footer = "e. Back"
    elif panel_mode == 2:
        header = "Inflict on:"
        options = []
        overlap = 0
        for x, unit in enumerate(enemy_player):
            if unit:
                if selected_ability not in unit.blocked_abilities:
                    options.append(f"{letters[x - overlap]}. {unit.trait} {unit.unit} ({unit.health} HP)")
                else:
                    overlap += 1
        footer = "e. Back"
    else:
        raise ValueError("Invalid panel mode.")
    return contruct_panel(header, options, footer)



def check_self_ability(selected_unit, ability):
    self_abilities = {
        "enrage": lambda: selected_unit.enrage(),
        "harden": lambda: selected_unit.harden(),
        "healSelf": lambda: selected_unit.heal_self(),
        "regen": lambda: selected_unit.regen()
    }
    if ability not in self_abilities:
        return False
    self_abilities[ability]()
    return True


def check_inflicting_ability(selected_unit, ability, selected_target):
    inflicting_abilities = {
        "attack": lambda: selected_target.damage(selected_unit.attack),
        "burn": lambda: selected_target.burn(),
        "leech": lambda: (
            selected_unit.heal(selected_target._health * 0.05),
            selected_target.true_damage(selected_target._health * 0.10),
        ),
        "pierce": lambda: selected_target.pierce(),
        "poison": lambda: selected_target.poison(),
        "weaken": lambda: selected_target.weaken(),
    }
    if ability not in inflicting_abilities:
        return False
    inflicting_abilities[ability]()
    return True


def convert_player_deck(deck, units_data):
    deck_units_idx = [gu.get_unit_idx(unit_slot, units_data) for unit_slot in deck]
    return [uc.Unit(units_data, *unit_idx) for unit_idx in deck_units_idx]


def contruct_panel(header, options, footer):
    if len(options) < 4:
        options.extend(["" for _ in range(4 - len(options))])
    options.append(footer)
    return {
        "header": header,
        "options": options
    }