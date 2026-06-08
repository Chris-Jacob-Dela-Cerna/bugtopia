

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
    ui_data = {
        "header": "Main Menu",
        "options": {
            "a": "Play 1v1",
            "b": "Credits",
            "c": "Quit"
        },
        "route": {
            "a": play_1v1,
            "b": credits,
            "c": sys.exit
        }
    }
    menu_ui = convert_data_ui(ui_data)

    while True:
        display(menu_ui)
        chosen = input("                 >>> ")
        if chosen in ui_data["options"]:
            while True:
                ui_data["route"][chosen]()
                break


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
    for row in ui:
        print(row)


def play_1v1():
    ui_data = {
        "header": "Main Menu",
        "options": {
            "a": "Create a Deck",
            "b": "Select an Existing Deck",
            "c": "Back"
        },
        "route": {
            "a": create_deck,
            "b": select_deck,
        }
    }


def credits():
    print("To be implemented.")


def create_deck():
    ...


def select_deck():
    print("To be implemented.")


if __name__ == "__main__":
    main()