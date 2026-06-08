

import sys


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
        },
        "route": {
            "a": play_1v1,
            "b": credits,
            "c": quit_game
        }
    }
    menu_ui = convertData_ui(menuData)

    while True:
        display(menu_ui)
        chosen = input("                 >>> ")
        if chosen in menuData["options"]:
            if menuData["route"][chosen]():
                break


def convertData_ui(uiData):
    ui = []
    ui.append("               ╭──────────────────────────────╮")
    ui.append("               │ " + uiData["header"] + ((28 - len(uiData["header"])) * " ") + " |")
    ui.append("               |──────────────────────────────|")

    space = 5
    for letter, option in uiData["options"].items():
        space -= 1
        ui.append("               │ " + letter + ". " + option + ((25 - len(option)) * " ") + " |")

    for _ in range(space):
        ui.append("               │                              |")
    ui.append("               ╰──────────────────────────────╯")
    return ui


def display(ui):
    for row in ui:
        print(row)


def play_1v1():
    print("Play 1v1")


def credits():
    print("Credits")


def quit_game():
    sys.exit()


if __name__ == "__main__":
    main()