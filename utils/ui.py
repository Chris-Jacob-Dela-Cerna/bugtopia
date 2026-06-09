

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
    ui.append("               ╭──────────────────────────────╮")
    ui.append("               │ " + ui_data["header"] + ((28 - len(ui_data["header"])) * " ") + " |")
    ui.append("               |──────────────────────────────|")

    space = 5
    for letter, option in ui_data["options"].items():
        space -= 1
        ui.append("               │ " + letter + ". " + option + ((25 - len(option)) * " ") + " |")

    for _ in range(space):
        ui.append("               │                              |")
    ui.append("               ╰──────────────────────────────╯")
    return ui


def convert_data_ui_player(ui_data, idx=0):
    page = ui_data[idx]
    ui = []
    ui.append("  ╭────────────────────────────────────────────────────────╮")
    ui.append("  | Create your deck:                                      |")
    ui.append("  |────────────────────────────────────────────────────────|")

    spc = 52
    ui.append("  | " + str(page["idx"] + 1) + ") " + page["name"] + (((spc - len(page["name"])) - len(str(page["idx"])))) * " " + " |")
    ui.append("  | Traits:                                                |")

    for num in range(3):
        print(page["traits"][num - 1])


    return ui


def display(ui):
    print("\n".join(ui))