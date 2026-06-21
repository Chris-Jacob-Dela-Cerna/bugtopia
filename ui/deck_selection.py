

from utils.ui_helpers import fit


def render_deck_ui(show_help):
    ui = []
    ui.append(f"{"\n" * 35}")
    ui.append("           ╭──────────────────────────────────────╮")
    ui.append("           | Select your deck:                    |")
    ui.append("           |──────────────────────────────────────|")




    ui.append("           |──────────────────────────────────────|")

    ui.append("           ╰──────────────────────────────────────╯")

    ui.extend(get_help_state(show_help))
    return ui


def get_help_state(show_help):
    if show_help:
        return [
            "             To change page -> type 'q', 'e'"
            "             To select -> type 'f'"
            "             To go back -> type 'b'"
        ]
    else:
        return ["             Type 'h' to view all options."]