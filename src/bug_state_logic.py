

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


def check_winner(decks, deck1, deck2):
    if all(x is None for x in decks):
        return "      It's tied!      "
    elif all(x is None for x in deck1):
        return "    Player 2 wins!    "
    elif all(x is None for x in deck2):
        return "    Player 1 wins!    "
    else:
        return False


def check_self_ability(selected_unit, selected_ability):
    if selected_ability in selected_unit.all_self_abilities:
        if selected_unit.apply_self(selected_ability):
            return True
    return False


def check_inflicting_ability(selected_unit, selected_ability, selected_target):
    if selected_target.apply_inflict(selected_unit, selected_ability):
        return True
    return False