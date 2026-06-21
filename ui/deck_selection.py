

from utils.ui_helpers import fit


def render_deck_ui(decks_data, idx, show_help):
    deck = decks_data[idx]
    ui = []
    ui.append(f"{"\n" * 35}")
    ui.append("           ╭──────────────────────────────────────╮")
    ui.append("           | Select your deck:                    |")

    ui.append("           |──────────────────────────────────────|")
    ui.extend(convert_deck_data(deck))
    ui.append("           |──────────────────────────────────────|")

    current_page = idx + 1
    total_pages = len(decks_data)
    back_option, next_option = get_page_option(current_page, total_pages)
    ui.append(fit(f"{current_page}/{total_pages}", 11, back_option, next_option))

    ui.append("           ╰──────────────────────────────────────╯")
    ui.extend(get_help_state(show_help))
    return ui


example = {
    "name": "Deck Name",
    "deck": [
        "bug",
        "bug2",
        "bug3"
    ]
}


def convert_deck_data(deck):
    rows = []
    rows.append(fit(f"", 36, "            | ", " |"))
    for bug in deck['deck']:
        rows.append(fit(bug, 34, "            | - ", " |"))
    return rows


def get_page_option(current_page, total_pages):
    if current_page == 1:
        back_option = "           |         | Page "
    else:
        back_option = "           | <<< (q) | Page "
    if current_page == total_pages:
        next_option = " |         |"
    else:
        next_option = " | (e) >>> |"
    return back_option, next_option


def get_help_state(show_help):
    if show_help:
        return [
            "             To change page -> type 'q', 'e'"
            "             To select -> type 'f'"
            "             To go back -> type 'b'"
        ]
    else:
        return ["             Type 'h' to view all options."]