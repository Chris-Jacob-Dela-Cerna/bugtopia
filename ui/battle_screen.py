

from utils.ui_helpers import fit


def convert_battle_ui(deck1, deck2):
    ui = []
    ui.append("  ╭────────────────────────────────────────────────────────╮")
    ui.append("  | Player 1                                               |")
    ui.append("  |────────────────────────────────────────────────────────|")

    unit_row = "  | "
    for idx in range(len(deck1)):
        if deck1[idx] == None:
            unit_row += "--            -- | "
        else:
            visible_idx = idx + 1
            unit_name = deck1[idx].unit
            unit_space = fit(13, unit_name)
            unit_row += f"{visible_idx}) {unit_name}{unit_space} | "
    ui.append(unit_row)

    trait_row = "  | "
    for idx in range(len(deck1)):
        if deck1[idx] == None:
            trait_row += "   --      --    | "
        else:
            trait_name = deck1[idx].trait
            trait_space = fit(13, trait_name)
            trait_row += f"T: {trait_name}{trait_space} | "
    ui.append(trait_row)

    health_row = "  | "
    for idx in range(len(deck1)):
        if deck1[idx] == None:
            health_row += "       --        | "
        else:
            health = deck1[idx].health
            base_health = deck1[idx].base_health
            health_space = fit(13, f"{health}/{base_health}")
            health_row += f"H: {health}/{base_health}{health_space} | "
    ui.append(health_row)


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