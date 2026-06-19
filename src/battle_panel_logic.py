

def get_control_panel_data(attacker, defender, panel_mode=0, unit=None, ability=None):
    letters = "abcd"

    if panel_mode == 1:
        header = "Choose an ability:"
        options = [f"{letters[x]}. {ability}" for x, ability in enumerate(unit.abilities) if ability not in unit.blocked_abilities]
        footer = "e. Back"


    elif panel_mode == 2:
        header = "Inflict on:"
        options = []
        for x, unit in enumerate(defender):
            if unit:
                if ability not in unit.blocked_abilities:
                    options.append(f"{letters[x]}. {unit.trait} {unit.unit} ({unit.health} HP)")
        footer = "e. Back"
    else:
        raise ValueError("Invalid panel mode.")
    return contruct_panel(header, options, footer)


def selection_panel(attacker):
    letters =    "abcd"
    header =     "Select a unit:"
    options =    {}
    ui_options = []
    footer =     "e. Skip"
    for x, unit in enumerate(attacker):
        if unit:
            options[letters[x]] = unit
            ui_options.append(f"{letters[x]}. {unit.trait} {unit.unit} ({unit.health} HP)")
    panel = contruct_panel(header, options, footer)
    return panel, options





def contruct_panel(header, options, footer):
    if len(options) < 4:
        options.extend(["" for _ in range(4 - len(options))])
    options.append(footer)
    return {
        "header": header,
        "options": options
    }