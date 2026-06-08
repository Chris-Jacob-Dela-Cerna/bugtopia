

def show_title():
    print(
    r"  __             __    __    __               __ " "\n"
    r" /\ \           /\ \__/\ \__/\ \             /\_\ " "\n"
    r" \ \ \___   ____\ \ ,_\ \ ,_\ \ \  ___   ____\/_/_   ____ " "\n"
    r"  \ \ '__`\/'__`\\ \ \/\ \ \/\ \ \/'__`\/\ '__`\\ \ /'__`\ " "\n"
    r"   \ \ \_\ \ \_\ \\ \ \_\ \ \_\ \ \ \_\ \ \ \_\ \\ \\ \_\ \ " "\n"
    r"    \ \____/\___` \\ \__\\ \__\\ \_\____/\ \ ,__/ \_\\___` \ " "\n"
    r"     \/___/ \___\__\\/__/ \/__/ \/_/___/  \ \ \/ \/_/\___\__\ " "\n"
    r"                \__/                       \ \_\         \__/" "\n"
    r"                                            \/_/" 
    )


def convert_data_ui(ui_data):
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


def display(ui):
    print("\n".join(ui))