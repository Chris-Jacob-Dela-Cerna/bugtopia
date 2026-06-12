

from utils.ui_helpers import fit


def prompt(message):
    ui = []
    ui.append("               ╭──────────────────────────────╮")
    message_space = fit(28, message)
    ui.append(f"               │ {message}{message_space} |")
    ui.append("               ╰──────────────────────────────╯")
    return ui