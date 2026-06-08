

def main():
    show_title()
    menu()


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


def menu():
    menuData = {
        "header": "Main Menu",
        "options": {
            "a": "Play 1v1",
            "b": "Credits",
            "c": "Quit"
        }
    }
    menu_ui = convertTo_ui(menuData)
    for _ in menu_ui:
        print(_)


def convertTo_ui(uiData):
    display = []
    display.append("               ╭──────────────────────────────╮")
    display.append("               │ " + uiData["header"] + ((28 - len(uiData["header"])) * " ") + " |")
    display.append("               |──────────────────────────────|")
    for letter, option in uiData["options"].items():
        display.append("               │ " + letter + ". " + option + ((25 - len(option)) * " ") + " |")
    display.append("               ╰──────────────────────────────╯")
    return display


if __name__ == "__main__":
    main()