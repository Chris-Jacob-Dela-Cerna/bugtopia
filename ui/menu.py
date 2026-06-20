

from utils.ui_helpers import fit


def render_menu_ui(ui_data):
    ui = []
    ui.append("               ╭──────────────────────────────╮")
    ui.append(fit(ui_data['header'], 28, "               │ ", " |"))
    ui.append("               |──────────────────────────────|")

    option_list = get_options(ui_data)
    ui.extend(option_list)

    blank_option = 5 - len(option_list)
    ui.extend(["               │                              |" for _ in range(blank_option)])
    ui.append("               ╰──────────────────────────────╯")
    return ui


def get_options(ui_data):
    option_list = []
    options = ui_data['options'].items()
    for letter, option in options:
        option_list.append(fit(f"{letter}. {option}", 28, "               │ ", " |"))
    return option_list