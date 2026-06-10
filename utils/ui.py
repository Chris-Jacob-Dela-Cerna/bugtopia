

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
    header = ui_data["header"]
    header_space = fit(28, ui_data["header"])
    ui.append("               ╭──────────────────────────────╮")
    ui.append(f"               │ {header}{header_space} |")
    ui.append("               |──────────────────────────────|")

    blank_option = 5
    options = ui_data["options"].items()
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
    ui.append("  | " + str(page["idx"] + 1) + ") " + page["name"] + ((((52 - len(page["name"])) - len(str(page["idx"])))) * " ") + " |")
    ui.append("  | Traits:                                                |")

    letters = "abc"
    rowTrait = "  |"
    rowHp = "  |"
    rowDef = "  |"
    rowAtk = "  |"
    listAbi = []
    for x in range(3):
        curTrait = page["traits"][x]
        rowTrait += " " + letters[x] + ". " + curTrait["trait"].title() + ((13 - len(curTrait["trait"])) * " ") + " |"
        curStat = curTrait["stats"]
        rowHp += " " + "HP: " + str(curStat["health"]) + ((12 - len(str(curStat["health"]))) * " ") + " |"
        rowDef += " " + "DEF: " + str(curStat["defence"]) + ((11 - len(str(curStat["defence"]))) * " ") + " |"
        rowAtk += " " + "ATK: " + str(curStat["attack"]) + ((11 - len(str(curStat["attack"]))) * " ") + " |"
        tempAbi = [_ for _ in curTrait["abilities"]]
        listAbi.append(tempAbi)
    ui.append(rowTrait)
    ui.append(rowHp)
    ui.append(rowDef)
    ui.append(rowAtk)

    ui.append("  | Abilities:                                             |")
    displayAbi = ["  |", "  |", "  |", "  |"]
    for z in range(3):
        for y in range(len(listAbi[z])):
            if len(listAbi[z][y]) == 0:
                displayAbi[y] += "                  |"
                continue
            displayAbi[y] += " - " + listAbi[z][y] + ((14 - len(listAbi[z][y])) * " ") + " |"
    for ability in displayAbi:
        ui.append(ability)
    ui.append("  |────────────────────────────────────────────────────────|")


    return ui


def fit(max_length, text_length):
    return (max_length - len(text_length)) * " "


def display(ui):
    print("\n".join(ui))