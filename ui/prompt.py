

from utils.ui_helpers import fit


def prompt(message):
    ui = []
    ui.append("               ╭──────────────────────────────╮")
    ui.append(fit(message, 28, "               │ ", " |"))
    ui.append("               ╰──────────────────────────────╯")
    return ui