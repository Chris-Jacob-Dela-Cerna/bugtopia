

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


def check_inflicting_ability(selected_unit, selected_ability, selected_target):
    if selected_unit.apply(selected_ability):
        return True
    elif selected_unit == "leech":
        selected_unit.heal(selected_target._health * 0.05)
        selected_target.true_damage(selected_target._health * 0.10)
        return True
    return False