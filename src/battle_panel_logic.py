

def get_control_panel_data(current_player, enemy_player, panel_mode=0, unit=None, ability=None):
    letters = "abcd"
    if panel_mode == 0:
        header = "Select a unit:"
        options = [f"{letters[x]}. {unit.trait} {unit.unit} ({unit.health} HP)" for x, unit in enumerate(current_player) if unit]
        footer = "e. Skip"


    elif panel_mode == 1:
        header = "Choose an ability:"
        options = [f"{letters[x]}. {ability}" for x, ability in enumerate(unit.abilities) if ability not in unit.blocked_abilities]
        footer = "e. Back"


    elif panel_mode == 2:
        header = "Inflict on:"
        options = []
        for x, unit in enumerate(enemy_player):
            if unit:
                if ability not in unit.blocked_abilities:
                    options.append(f"{letters[x]}. {unit.trait} {unit.unit} ({unit.health} HP)")
        footer = "e. Back"
    else:
        raise ValueError("Invalid panel mode.")
    return contruct_panel(header, options, footer)


def contruct_panel(header, options, footer):
    if len(options) < 4:
        options.extend(["" for _ in range(4 - len(options))])
    options.append(footer)
    return {
        "header": header,
        "options": options
    }