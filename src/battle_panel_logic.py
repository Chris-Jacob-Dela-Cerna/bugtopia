

def selection_panel(attacker):
    letters =    "abcd"
    header =     "Select a bug:"
    options =    {}
    ui_options = []
    footer =     "e. Skip"

    for x, bug in enumerate(attacker):
        if bug:
            options[letters[x]] = bug
            ui_options.append(f"{letters[x]}. {bug.species} {bug.family} ({bug.health} HP)")
    panel = contruct_panels(header, ui_options, footer)
    return panel, options


def ability_panel(selected_bug):
    letters =    "abcd"
    header =     "Choose an ability:"
    options =    {}
    ui_options = []
    footer =     "e. Back"
    
    for x, ability in enumerate(selected_bug.active_abilities):
        if ability:
            options[letters[x]] = ability
            ui_options.append(f"{letters[x]}. {ability}")
    panel = contruct_panels(header, ui_options, footer)
    return panel, options


def attack_panel(defender, selected_ability):
    letters =    "abcd"
    header =     "Inflict on:"
    options =    {}
    ui_options = []
    footer =     "e. Back"

    for x, bug in enumerate(defender):
        if bug:
            if selected_ability not in bug.active_effects:
                options[letters[x]] = bug
                ui_options.append(f"{letters[x]}. {bug.species} {bug.family} ({bug.health} HP)")
    panel = contruct_panels(header, ui_options, footer)
    return panel, options


def contruct_panels(header, options, footer):
    if len(options) < 4:
        options.extend(["" for _ in range(4 - len(options))])
    options.append(footer)
    return {
        "header": header,
        "options": options
    }