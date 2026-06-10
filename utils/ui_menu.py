

from utils.ui_helpers import fit


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