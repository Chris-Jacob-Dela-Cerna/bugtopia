

from utils.ui_helpers import fit


def render_page_ui(ui_data, idx=0, deck=[], show_help=False):
    page = ui_data[idx]
    ui = []
    ui.append(f"{"\n" * 30}")
    ui.append("  ╭────────────────────────────────────────────────────────╮")
    ui.append("  | Create your deck:                                      |")
    ui.append("  |────────────────────────────────────────────────────────|")

    current_page = page['idx'] + 1
    ui.append(fit(f"{current_page}) {page['name']}", 54, "  | ", " |"))

    ui.append("  | Bugs:                                                  |")
    ui.extend(convert_bug_stats_ui(page))

    ui.append("  | Abilities:                                             |")
    ability_list = get_abilities(page)
    ui.extend(convert_abilities_ui(ability_list))

    ui.append("  |────────────────────────────────────────────────────────|")
    total_pages = len(ui_data)
    back_option, next_option = get_page_option(current_page, total_pages)
    ui.append(fit(f"{current_page}/{total_pages}", 11, "  | Page ", f" | {back_option} | {next_option} |"))

    ui.append("  |────────────────────────────────────────────────────────|")
    slots = get_slots(deck)
    ui.append(f"  | {slots[0]} | {slots[1]} | {slots[2]} |")
    ui.append("  ╰────────────────────────────────────────────────────────╯")

    ui.extend(get_help_state(show_help))
    return ui


def convert_bug_stats_ui(page):
    options = "abc"
    rows = ["  |", "  |", "  |", "  |"]
    for x in range(3):
        current_species = page['species'][x]
        rows[0] += fit(f"{options[x]}. {current_species['name'].title()}", 16, " ", " |")
        rows[1] += fit(current_species['stats']['health'], 12, " HP: ", " |")
        rows[2] += fit(current_species['stats']['defence'], 11, " DEF: ", " |")
        rows[3] += fit(current_species['stats']['attack'], 11, " ATK: ", " |")
    return rows


def get_abilities(page):
    ability_list = []
    for x in range(3):
        ability_list.append([_ for _ in page['species'][x]['abilities']])
    return ability_list


def convert_abilities_ui(ability_list):
    abilities = ["  |", "  |", "  |", "  |"]
    for x, ability_row in enumerate(ability_list):
        for y, ability in enumerate(ability_row):
            if not bool(ability):
                abilities[y] += "                  |"
                continue
            abilities[y] += fit(ability, 14, " - ", " |")
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
        slots.append(fit(slot, 16))
    empty_slots = 3 - len(deck)
    if empty_slots:
        slots.extend(["---             " for _ in range(empty_slots)])
    return slots


def get_help_state(show_help):
    if show_help:
        return [
            "    To change page -> type 'e', 'r', or the page number", 
            "    To select -> type unit-bug, ex: '1b', 2a, or '3c'", 
            "    To undo -> type 'd'",
            "    To finish -> type 'f'",
            "    To go back -> type 'b'"
        ]
    else:
        return ["    Type 'h' to view all options."]