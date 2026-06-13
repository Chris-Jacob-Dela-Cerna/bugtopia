

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
        unit = units_data[unit_idx]

        unit_name = unit['name']
        if len(unit_name) > 1 or len(unit_name) > 13:
            raise ValueError("Invalid unit name length. Range: 1-13")
        self._unit = unit_name

        trait = unit['traits'][trait_idx]

        trait_name = trait['name']
        if len(trait_name) < 1 or len(trait_name) > 13:
            raise ValueError("Invalid trait name length. Range: 1-13")
        self._trait = trait_name

        health = trait['stats']['health']
        if health < 1 or health > 9999999:
            raise ValueError("Invalid health value. Range: 1-9999999")
        self.health = health

        defence = trait['stats']['defence']
        if defence < 1 or defence > 9999999:
            raise ValueError("Invalid defence value. Range: 1-9999999")
        self.defence = defence

        attack = trait['stats']['attack']
        if attack < 1 or attack > 9999999:
            raise ValueError("Invalid attack value. Range: 1-9999999")
        self.attack = attack

        abilities = trait['abilities']
        self.can_attack = False
        if "attack" in abilities:
            self.can_attack = True
        self.can_healSelf = False
        if "healSelf" in abilities:
            self.can_healSelf = True

    @property
    def unit(self):
        return self._unit
    
    @property
    def trait(self):
        return self._trait