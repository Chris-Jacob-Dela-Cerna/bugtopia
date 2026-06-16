

from utils.ui_helpers import fit


def convert_battle_ui(current_deck, enemy_deck):
    ui = []
    ui.append("  ╭────────────────────────────────────────────────────────╮")
    ui.append("  | Player 1                                               |")
    ui.append("  |────────────────────────────────────────────────────────|")

    ui.extend(get_deck_rows(enemy_deck))

    ui.append("  ╰────────────────────────────────────────────────────────╯")
    ui.append("                            Turn 1")
    ui.append("  ╭────────────────────────────────────────────────────────╮")

    ui.extend(get_deck_rows(current_deck))

    ui.append("  |────────────────────────────────────────────────────────|")
    ui.append("  | Player 2                                               |")
    ui.append("  |────────────────────────────────────────────────────────|")

    ui.extend(get_control_panel_rows(control_panel_data))

    ui.append("  ╰────────────────────────────────────────────────────────╯")
    return ui


def get_deck_rows(deck):
    rows = ["  | ", "  | ", "  | ", "  | ", "  | ", "  | ", "  | "]
    dead_cells = [
        "--            -- | ",
        "   --      --    | ",
        "       --        | ",
        "     --  --      | ",
        "       --        | ",
        "   --      --    | ",
        "--            -- | "
    ]
    for x, row in enumerate(rows):
        for y, slot in enumerate(deck):
            if slot == None:
                row += dead_cells[x]
                rows[x] = row
                continue
            elif x == 0:
                row += fit(slot.unit, 13, f"{y + 1}) ", " | ") 
            elif x == 1:
                row += fit(slot.trait, 13, "T: ", " | ")
            elif x == 2:
                row += fit(f"{slot.health}/{slot.base_health}", 13, "H: ", " | ")
            elif x == 3:
                row += fit(slot.defence, 11, "DEF: ", " | ")
            elif x == 4:
                row += fit(slot.attack, 11, "ATK: ", " | ")
            elif x == 5:
                buffs = slot.show_buffs()
                if len(buffs) > 11:
                    buffs = buffs[:11]
                row += fit(buffs, 11, "BUF: ", " | ")
            elif x == 6:
                debuffs = slot.show_debuffs()
                if len(debuffs) > 11:
                    debuffs = debuffs[:11]
                row += fit(debuffs, 11, "DBF: ", " | ")
            rows[x] = row
    return rows


control_panel_data = {
    "header": "Select a unit:",
    "options": [
        "a. ",
        "b. ",
        "",
        "",
        "e. Back"
    ]
}


def get_control_panel_rows(control_panel_data):
    rows = []
    rows.append(fit(control_panel_data['header'], 54, "  | " ," |"))

    blank_cell = "                                                       |"

    return rows