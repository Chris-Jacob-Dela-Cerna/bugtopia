

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


def check_self_ability(selected_unit, ability):
    self_abilities = {
        "enrage": lambda: selected_unit.enrage(),
        "harden": lambda: selected_unit.harden(),
        "healSelf": lambda: selected_unit.heal_self(),
        "regen": lambda: selected_unit.regen()
    }
    if ability in self_abilities:
        self_abilities[ability]()
        return True
    return False


def check_inflicting_ability(selected_unit, ability, selected_target):
    inflicting_abilities = {
        "attack": lambda: selected_target.damage(selected_unit.attack),
        "burn": lambda: selected_target.burn(),
        "leech": lambda: (
            selected_unit.heal(selected_target._health * 0.05),
            selected_target.true_damage(selected_target._health * 0.10),
        ),
        "pierce": lambda: selected_target.pierce(),
        "poison": lambda: selected_target.poison(),
        "weaken": lambda: selected_target.weaken(),
    }
    if ability in inflicting_abilities:
        inflicting_abilities[ability]()
        return True
    return False