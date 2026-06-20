

def run_per_instance_checks(decks):
    for deck in decks:
        for x, unit in enumerate(deck):
            if unit:
                unit.per_instance_checks()
                if not unit._vital_status['alive']:
                    deck[x] = None


def run_per_turn_checks(decks):
    for deck in decks:
        for x, unit in enumerate(deck):
            if unit:
                unit.per_turn_checks()
                if not unit._vital_status['alive']:
                    deck[x] = None


def check_self_ability(selected_unit, selected_ability):
    self_abilities = ["enrage", "harden", "healSelf", "regen", "shell"]
    if selected_ability in self_abilities:
        if selected_unit.apply(selected_ability):
            return True
    return False


def check_inflicting_ability(selected_unit, selected_ability, selected_target):
    instant_abilities = {
        "attack":    lambda: selected_target.damage(selected_unit.attack),
        "leech":     lambda: (
            selected_unit.heal(selected_target._health * 0.5),
            selected_target.true_damage(selected_target._health * 0.15),
        ),
        "sacrifice": lambda: (
            selected_target.damage(selected_unit._health * 0.30),
            selected_unit.true_damage(selected_unit._health * 0.30)
        ),
        "sting":     lambda: selected_target.true_damage(selected_target._health * 0.20)
    }
    if selected_ability in instant_abilities:
        instant_abilities[selected_ability]()
        return True
    elif selected_target.apply(selected_ability):
        return True
    return False