

from utils.ui_helpers import fit


def convert_battle_ui(deck1, deck2):
    ui = []
    ui.append("  ╭────────────────────────────────────────────────────────╮")
    ui.append("  | Player 1                                               |")
    ui.append("  |────────────────────────────────────────────────────────|")

    deck1_rows = get_deck_rows(deck1)
    ui.extend(deck1_rows)

    ui.append("  |────────────────────────────────────────────────────────|")
    ui.append("  |                                                        |")
    ui.append("  |────────────────────────────────────────────────────────|")

    deck2_rows = get_deck_rows(deck2)
    ui.extend(deck2_rows)

    ui.append("  |────────────────────────────────────────────────────────|")
    ui.append("  | Player 2                                               |")
    ui.append("  ╰────────────────────────────────────────────────────────╯")
    ui.append("  ╭────────────────────────────────────────────────────────╮")



    ui.append("  ╰────────────────────────────────────────────────────────╯")
    return ui


def get_deck_rows(deck):
    rows = ["  | ", "  | ", "  | ", "  | ", "  | ", "  | "]
    dead_rows = [
        "--            -- | ",
        "   --      --    | ",
        "       --        | ",
        "       --        | ",
        "   --      --    | ",
        "--            -- | "
    ]
    for x, row in enumerate(rows):
        for y, slot in enumerate(deck):
            if slot == None:
                row += dead_rows[x]
                rows[x] = row
                continue
            elif x == 0:
                row += fit2(slot.unit, 13, f"{y + 1}) ", " | ") 
            elif x == 1:
                row += fit2(slot.trait, 13, "T: ", " | ")
            elif x == 2:
                row += fit2(f"{slot.health}/{slot.base_health}", 13, "H: ", " | ")
            elif x == 3:
                row += fit2(slot.defence, 11, "DEF: ", " | ")
            elif x == 4:
                row += fit2(slot.attack, 11, "ATK: ", " | ")
            elif x == 5:
                row += "                 | "
            rows[x] = row
    return rows


def fit2(text="", total_space=0, first="", last=""):
    space = (total_space - len(str(text))) * " "
    return f"{first}{text}{space}{last}"