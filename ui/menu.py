

from utils.ui_helpers import fit


def convert_data_ui_menu(ui_data):
    ui = []
    header = ui_data['header']
    header_space = fit(28, ui_data['header'])
    ui.append("               ╭──────────────────────────────╮")
    ui.append(f"               │ {header}{header_space} |")
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
        option_space = fit(25, option)
        option_list.append(f"               │ {letter}. {option}{option_space} |")
    return option_list