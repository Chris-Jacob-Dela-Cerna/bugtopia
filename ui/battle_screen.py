

from utils.ui_helpers import fit


def render_battle_ui(attacker, defender, control_panel, state):
    ui = []
    ui.append(f"{"\n" * 35}")
    ui.append("  ╭────────────────────────────────────────────────────────╮")
    ui.append(f"  | Player {state[1][1]} (Enemy)                                       |")
    ui.append("  |────────────────────────────────────────────────────────|")

    ui.extend(get_deck_rows(defender))

    ui.append("  ╰────────────────────────────────────────────────────────╯")
    ui.append(f"  Turn {state[0]}")
    ui.append("  ╭────────────────────────────────────────────────────────╮")

    ui.extend(get_deck_rows(attacker))

    ui.append("  |────────────────────────────────────────────────────────|")
    ui.append(f"  | Player {state[1][0]} (You)                                         |")
    ui.append("  |────────────────────────────────────────────────────────|")

    ui.extend(get_control_panel_rows(control_panel))

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
                row += fit(slot.family, 13, f"{y + 1}) ", " | ") 
            elif x == 1:
                row += fit(slot.species, 13, "S: ", " | ")
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


def get_control_panel_rows(control_panel_data):
    rows = []
    rows.append(fit(control_panel_data['header'], 54, "  | " ," |"))

    blank_cell = "                                                       |"
    for option in control_panel_data['options']:
        if option:
            rows.append(fit(option, 54, "  | ", " |"))
        else:
            rows.append(fit(blank_cell, first="  | "))
    return rows