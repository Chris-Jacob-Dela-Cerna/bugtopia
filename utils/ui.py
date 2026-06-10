

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


def convert_data_ui_player(ui_data, idx=1, deck=[]):
    page = ui_data[idx]

    ui = []
    ui.append("  ╭────────────────────────────────────────────────────────╮")
    ui.append("  | Create your deck:                                      |")
    ui.append("  |────────────────────────────────────────────────────────|")

    page_idx = page['idx'] + 1
    page_name = page['name']
    unit_space = fit(52, f"{page_idx}{page_name}")
    ui.append(f"  | {page_idx}) {page_name}{unit_space} |")
    ui.append("  | Traits:                                                |")

    options = "abc"
    rows = ["  |", "  |", "  |", "  |"]
    rowTrait = "  |"
    rowHp = "  |"
    rowDef = "  |"
    rowAtk = "  |"
    ability_list = []



    for x in range(3):
        current_trait = page['traits'][x]
        trait = current_trait['trait']
        trait_space = fit(13, trait)
        rowTrait += f" {options[x]}. {trait.title()}{trait_space} |"

        health = current_trait['stats']['health']
        defence = current_trait['stats']['defence']
        attack = current_trait['stats']['attack']
        health_space = fit(12, health)
        defence_space = fit(11, defence)
        attack_space = fit(11, attack)
        rowHp += f" HP: {health}{health_space} |"
        rowDef += f" DEF: {defence}{defence_space} |"
        rowAtk += f" ATK: {attack}{attack_space} |"

        abilities = current_trait['abilities']
        ability_list.append([_ for _ in abilities])

    ui.append(rowTrait)
    ui.append(rowHp)
    ui.append(rowDef)
    ui.append(rowAtk)

    ui.append("  | Abilities:                                             |")
    displayAbi = ["  |", "  |", "  |", "  |"]
    for z in range(3):
        for y in range(len(ability_list[z])):
            if len(ability_list[z][y]) == 0:
                displayAbi[y] += "                  |"
                continue
            displayAbi[y] += " - " + ability_list[z][y] + ((14 - len(ability_list[z][y])) * " ") + " |"
    for ability in displayAbi:
        ui.append(ability)
    ui.append("  |────────────────────────────────────────────────────────|")


    return ui


def fit(max_length, text_length):
    return (max_length - len(str(text_length))) * " "


def display(ui):
    print("\n".join(ui))