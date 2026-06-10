

def show_title():
    input(
    r"  __             __    __    __               __ " "\n"
    r" /\ \           /\ \__/\ \__/\ \             /\_\ " "\n"
    r" \ \ \___   ____\ \ ,_\ \ ,_\ \ \  ___   ____\/_/_   ____ " "\n"
    r"  \ \ '__`\/'__`\\ \ \/\ \ \/\ \ \/'__`\/\ '__`\\ \ /'__`\ " "\n"
    r"   \ \ \_\ \ \_\ \\ \ \_\ \ \_\ \ \ \_\ \ \ \_\ \\ \\ \_\ \ " "\n"
    r"    \ \____/\___` \\ \__\\ \__\\ \_\____/\ \ ,__/ \_\\___` \ " "\n"
    r"     \/___/ \___\__\\/__/ \/__/ \/_/___/  \ \ \/ \/_/\___\__\ " "\n"
    r"                \__/                       \ \_\         \__/" "\n"
    r"                                            \/_/" "\n"
    )


def convert_data_ui_menu(ui_data):
    ui = []
    header = ui_data['header']
    header_space = fit(28, ui_data['header'])
    ui.append("               ╭──────────────────────────────╮")
    ui.append(f"               │ {header}{header_space} |")
    ui.append("               |──────────────────────────────|")

    blank_option = 5
    options = ui_data['options'].items()
    for letter, option in options:
        blank_option -= 1
        option_space = fit(25, option)
        ui.append(f"               │ {letter}. {option}{option_space} |")

    for _ in range(blank_option):
        ui.append("               │                              |")
    ui.append("               ╰──────────────────────────────╯")
    return ui


def convert_data_ui_player(ui_data, idx=0, deck=[]):
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

    return ui


def fit(max_length, text_length):
    return (max_length - len(str(text_length))) * " "


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
        back_option = "    <<< Back (k)"
    if current_page == total_pages:
        next_option = "                "
    else:
        next_option = "Next (l) >>>    "
    return back_option, next_option


def display(ui):
    print("\n".join(ui))