

from utils.ui_helpers import fit


def convert_battle_ui(deck1, deck2):
    ui = []
    ui.append("  ╭────────────────────────────────────────────────────────╮")
    ui.append("  | Player 1                                               |")
    ui.append("  |────────────────────────────────────────────────────────|")

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
        for y, slot in enumerate(deck1):
            if slot == None:
                row += dead_rows[x]
                continue
            elif x == 0:
                visible_idx = y + 1
                unit_name = slot.unit
                unit_space = fit(13, unit_name)
                row += f"{visible_idx}) {unit_name}{unit_space} | "
            elif x == 1:
                trait_name = slot.trait
                trait_space = fit(13, trait_name)
                row += f"T: {trait_name}{trait_space} | "
            elif x == 2:
                health = slot.health
                base_health = slot.base_health
                health_space = fit(13, f"{health}/{base_health}")
                row += f"H: {health}/{base_health}{health_space} | "
            elif x == 3:
                defence = slot.defence
                defence_space = fit(11, defence)
                row += f"DEF: {defence}{defence_space} | "
            elif x == 4:
                attack = slot.attack
                attack_space = fit(11, attack)
                row += f"ATK: {attack}{attack_space} | "
            else:
                row += "                 | "
            rows[x] = row

    ui.extend(rows)



    ui.append("  |────────────────────────────────────────────────────────|")
    ui.append("  |                                                        |")
    ui.append("  |────────────────────────────────────────────────────────|")



    ui.append("  |────────────────────────────────────────────────────────|")
    ui.append("  | Player 2                                               |")
    ui.append("  ╰────────────────────────────────────────────────────────╯")
    ui.append("  ╭────────────────────────────────────────────────────────╮")



    ui.append("  ╰────────────────────────────────────────────────────────╯")
    return ui