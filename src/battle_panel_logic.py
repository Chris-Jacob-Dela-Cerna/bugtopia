

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
    panel = contruct_panel(header, ui_options, footer)
    return panel, options


def ability_panel(selected_unit):
    letters =    "abcd"
    header =     "Choose an ability:"
    options =    {}
    ui_options = []
    footer =     "e. Back"
    
    for x, ability in enumerate(selected_unit.active_abilities):
        if ability:
            options[letters[x]] = ability
            ui_options.append(f"{letters[x]}. {ability}")
    panel = contruct_panel(header, ui_options, footer)
    return panel, options


def attack_panel(defender, selected_ability):
    letters =    "abcd"
    header =     "Inflict on:"
    options =    {}
    ui_options = []
    footer =     "e. Back"

    for x, unit in enumerate(defender):
        if unit:
            if selected_ability not in unit.active_effects:
                options[letters[x]] = unit
                ui_options.append(f"{letters[x]}. {unit.trait} {unit.unit} ({unit.health} HP)")
    panel = contruct_panel(header, ui_options, footer)
    return panel, options


def contruct_panel(header, options, footer):
    if len(options) < 4:
        options.extend(["" for _ in range(4 - len(options))])
    options.append(footer)
    return {
        "header": header,
        "options": options
    }