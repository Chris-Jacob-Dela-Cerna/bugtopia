

from utils.ui_helpers import fit


def convert_page_ui(ui_data, idx=0, deck=[], show_help=False):
    page = ui_data[idx]
    ui = []
    ui.append("  ╭────────────────────────────────────────────────────────╮")
    ui.append("  | Create your deck:                                      |")
    ui.append("  |────────────────────────────────────────────────────────|")

    current_page = page['idx'] + 1
    unit_name = page['name']
    unit_space = fit(52, f"{current_page}{unit_name}")
    ui.append(f"  | {current_page}) {unit_name}{unit_space} |")
    ui.append("  | Traits:                                                |")

    rows = convert_trait_stats_ui(page)
    ui.extend(rows)

    ability_list = get_abilities(page)
    ui.append("  | Abilities:                                             |")

    abilities = convert_abilities_ui(ability_list)
    ui.extend(abilities)
    ui.append("  |────────────────────────────────────────────────────────|")

    total_pages = len(ui_data)
    page_space = fit(10, f"{current_page}{total_pages}")
    back_option, next_option = get_page_option(current_page, total_pages)
    ui.append(f"  | Page {current_page}/{total_pages}{page_space} | {back_option} | {next_option} |")
    ui.append("  |────────────────────────────────────────────────────────|")

    slots = get_slots(deck)
    ui.append(f"  | {slots[0]} | {slots[1]} | {slots[2]} |")
    ui.append("  ╰────────────────────────────────────────────────────────╯")

    help_state = get_help_state(show_help)
    ui.extend(help_state)

    return ui


def convert_trait_stats_ui(page):
    options = "abc"
    rows = ["  |", "  |", "  |", "  |"]

    for x in range(3):
        current_trait = page['traits'][x]
        trait = current_trait['trait']
        trait_space = fit(13, trait)
        rows[0] += f" {options[x]}. {trait.title()}{trait_space} |"

        health = current_trait['stats']['health']
        defence = current_trait['stats']['defence']
        attack = current_trait['stats']['attack']
        health_space = fit(12, health)
        defence_space = fit(11, defence)
        attack_space = fit(11, attack)

        rows[1] += f" HP: {health}{health_space} |"
        rows[2] += f" DEF: {defence}{defence_space} |"
        rows[3] += f" ATK: {attack}{attack_space} |"

    return rows


def get_abilities(page):
    ability_list = []
    for x in range(3):
        abilities = page['traits'][x]['abilities']
        ability_list.append([_ for _ in abilities])
    return ability_list


def convert_abilities_ui(ability_list):
    abilities = ["  |", "  |", "  |", "  |"]
    for x in range(3):
        for y in range(len(ability_list[x])):
            current_ability = ability_list[x][y]
            if not bool(current_ability):
                abilities[y] += "                  |"
                continue
            ability_space = fit(14, current_ability)
            abilities[y] += f" - {current_ability}{ability_space} |"
    return abilities


def get_page_option(current_page, total_pages):
    if current_page == 1:
        back_option = "                "
    else:
        back_option = "    <<< Back (e)"
    if current_page == total_pages:
        next_option = "                "
    else:
        next_option = "Next (r) >>>    "
    return back_option, next_option


def get_slots(deck):
    slots = []
    for slot in deck:
        slot_space = fit(16, slot)
        slots.append(f"{slot}{slot_space}")
    empty_slot = 3 - len(deck)
    if empty_slot != 0:
        for _ in range(empty_slot):
            slots.append("---             ")
    return slots


def get_help_state(show_help):
    if show_help:
        return ["    To change page -> type 'e', 'r', or the page number", 
                "    To select -> type unit-trait, ex: '1b', 2a, or '3c'", 
                "    To undo -> type 'd'",
                "    To finish -> type 'f'",
                "    To go back -> type 'b'"
                ]
    else:
        return ["    Type 'h' to view all options."]