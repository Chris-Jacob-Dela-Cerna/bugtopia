

import re


def get_unit_idx(unit_slot, units_data):
    if not (unit_code := re.search(r"^T([1-3])-(.*)$", unit_slot)):
        raise ValueError("Invalid slot code.")

    unit_name = unit_code.group(2)
    unit_idx = None
    for idx, unit in enumerate(units_data):
        if unit_name == units_data[idx]['name']:
            unit_idx = idx
            break
    if unit_idx == None:
        raise ValueError("Invalid unit.")

    trait_idx = int(unit_code.group(1)) - 1
    return unit_idx, trait_idx