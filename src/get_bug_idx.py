

import re


def get_bug_idx(bug_slot, bugs_data):
    if not (bug_id := re.search(r"^T([1-3])-(.*)$", bug_slot)):
        raise ValueError("Invalid slot code.")

    family_name = bug_id.group(2)
    family_idx = None
    for idx, family in enumerate(bugs_data):
        if family_name == bugs_data[idx]['name']:
            family_idx = idx
            break
    if family_idx == None:
        raise ValueError("Invalid unit.")

    species_idx = int(bug_id.group(1)) - 1
    return family_idx, species_idx