

import re


def get_unit(slot, units_data):
    if not (unit := re.search(r"^T([1-3])-(.*)$", slot)):
        raise ValueError("Invalid slot code.")
    trait_idx = int(unit.group(1)) - 1
    unit_name = unit.group(2)
    
    unit_idx = None
    for idx in range(len(units_data)):
        if unit_name == units_data[idx]["name"]:
            unit_idx = idx
            break
    if not unit_idx:
        raise ValueError("Invalid unit.")

    return unit_idx, trait_idx


class Unit:
    def __init__(self, unit_idx, trait_idx, units_data):
        ...