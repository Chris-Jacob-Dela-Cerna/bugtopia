

import copy
from millify import millify


class Bug:
    ability_data = {
        "active": {
            "instant":      ["attack", "healSelf", "leech", "sacrifice", "sting"],
            "ticking": {
                "burn":     {"display": "BRN", "duration": 1, "ticks": 0},
                "enrage":   {"display": "RGE", "duration": 1, "ticks": 0},
                "harden":   {"display": "HRD", "duration": 1, "ticks": 0},
                "pierce":   {"display": "PRC", "duration": 3, "ticks": 0},
                "venom":   {"display": "PSN", "duration": 2, "ticks": 0},
                "regen":    {"display": "RGN", "duration": 2, "ticks": 0},
                "weaken":   {"display": "WKN", "duration": 2, "ticks": 0}
            },
        },
        "passive": {
            "lastStand":    {"display": "LST"},
        }
    }
    multipliers = {
        "burn":       {"health": 0, "defence": 0, "attack": 0},
        "enrage":     {"health": 0, "defence": 0, "attack": 0},
        "harden":     {"health": 0, "defence": 0, "attack": 0},
        "lastStand":  {"health": 0, "defence": 0, "attack": 0},
        "pierce":     {"health": 0, "defence": 0, "attack": 0},
        "venom":     {"health": 0, "defence": 0, "attack": 0},
        "regen":      {"health": 0, "defence": 0, "attack": 0},
        "weaken":     {"health": 0, "defence": 0, "attack": 0}
    }
    statuses = {
        "buffs":      ["enrage", "harden", "regen"],
        "debuffs":    ["burn", "pierce", "venom", "weaken" ]
    }
    def __init__(self, units_data, family_idx=0, species_idx=0):
        family = units_data[family_idx]
        family_name = family['name']
        if len(family_name) < 1 or len(family_name) > 13:
            raise ValueError("Invalid family name length. Range: 1-13")
        self._family = family_name
        

        species = family['species'][species_idx]
        species_name = species['name']
        if len(species_name) < 1 or len(species_name) > 13:
            raise ValueError("Invalid bug name length. Range: 1-13")
        self._species = species_name


        health = species['stats']['health']
        if health < 1 or health > 9999999:
            raise ValueError("Invalid health value. Range: 1-9999999")
        self._base_health = health
        self._health = health


        defence = species['stats']['defence']
        if defence < 0 or defence > 999999:
            raise ValueError("Invalid defence value. Range: 0-999999")
        self._base_defence = defence
        self._defence = defence


        attack = species['stats']['attack']
        if attack < 0 or attack > 999999:
            raise ValueError("Invalid attack value. Range: 0-9999999")
        self._base_attack = attack
        self._attack = attack


        abilities = species['abilities']
        self._abilities = abilities

        self._ability_data = copy.deepcopy(Bug.ability_data)
        self._multipliers = copy.deepcopy(Bug.multipliers)

        actives = self._ability_data['active']
        self._active_abilities = [ability for ability in abilities if ability in actives['instant'] or ability in actives['ticking']]
        self._passive_abilities = [ability for ability in abilities if ability in self._ability_data['passive']]

        self._active_buffs = []
        self._active_debuffs = []
        self._vital_status = {
            "full_hp": True,
            "alive": True
        }



    @property
    def family(self):
        return self._family.title()
    @property
    def species(self):
        return self._species.title()



    @property
    def base_health(self):
        return millify(self._base_health, precision=1)
    @property
    def health(self):
        return millify(self._health, precision=1)



    @property
    def base_defence(self):
        return self._base_defence
    @property
    def defence(self):
        base_multiplier = 1.00
        for ability in self.multipliers:
            if self._multipliers[ability]['defence']:
                base_multiplier += self._multipliers[ability]['defence']
        defence = self._defence * base_multiplier
        return round(defence)



    @property
    def base_attack(self):
        return self._base_attack
    @property
    def attack(self):
        base_multiplier = 1.00
        for ability in self._multipliers:
            if self._multipliers[ability]['attack']:
                base_multiplier += self._multipliers[ability]['attack']
        attack = self._attack * base_multiplier
        return round(attack)



    @property
    def abilities(self):
        return sorted(self._abilities)

    @property
    def active_abilities(self):
        return sorted(self._active_abilities)

    @property
    def passive_abilities(self):
        return sorted(self._passive_abilities)

    @property
    def active_effects(self):
        return sorted(self._active_buffs + self.active_debuffs)

    @property
    def active_buffs(self):
        return sorted(self._active_buffs)

    @property
    def active_debuffs(self):
        return sorted(self._active_debuffs)



    def show_buffs(self):
        statuses = []
        for buff in self._active_buffs:
            statuses.append(self._ability_data['active']['ticking'][buff]['display'])
        return self.compile_statuses(statuses)

    def show_debuffs(self):
        statuses = []
        for debuff in self._active_debuffs:
            statuses.append(self._ability_data['active']['ticking'][debuff]['display'])
        return self.compile_statuses(statuses)

    def compile_statuses(self, statuses):
        status_message = ""
        if statuses:
            for status in statuses:
                if status_message:
                    status_message += "|"
                status_message += status
        return status_message



    def can(self, ability):
        if ability in self._abilities:
            return True
        return False

    def apply(self, ability, damage=None):
        if ability in Bug.statuses['buffs']:
            self.add_buff(ability)
            return True
        elif ability in Bug.statuses['debuffs']:
            self.add_debuff(ability)
            return True
        match ability:
            case "attack":
                self.damage(damage)
                return True
            case "healSelf":
                self.healSelf()
                return True
        return False



    def per_instance_checks(self):
        self.check_vital_status()
        self.check_passives()
        self.gate_abilities()

    def per_turn_checks(self):
        self.check_effects()
        self.check_vital_status()
        self.check_passives()
        self.gate_abilities()



    def check_vital_status(self):
        self.check_if_alive()
        self.check_if_full_hp()

    def check_if_alive(self):
        if self._health <= 0:
            self._vital_status['alive'] = False

    def check_if_full_hp(self):
        if self._health == self._base_health:
            self._vital_status['full_hp'] = True
            self.add_active_ability("healSelf")
            self.add_active_ability("leech")
        else:
            self._vital_status['full_hp'] = False
            self.remove_active_ability("healSelf")
            self.remove_active_ability("leech")



    def check_effects(self):
        for effect in self.active_effects:
            self.apply_ticking_effect(effect)
            self.tick_effect(effect)

    def apply_ticking_effect(self, effect):
        match effect:
            case "burn":
                self.damage(self._base_health * 0.25)
            case "venom":
                self.venom_damage()
            case "regen":
                self.heal(self._base_health * 0.10)

    def tick_effect(self, ability):
        ticks = self._ability_data['active']['ticking'][ability]['ticks']
        if ticks > 0:
            self._ability_data['active']['ticking'][ability]['ticks'] -= 1
        if ticks == 0:
            if ability in Bug.statuses['buffs']:
                self.remove_buff(ability)
            elif ability in Bug.statuses['debuffs']:
                self.remove_debuff(ability)



    def check_passives(self):
        for ability in self._passive_abilities:
            match ability:
                case "lastStand":
                    self.lastStand()

    def lastStand(self):
        if self._health < self._base_health * 0.30:
            self.add_multiplier_effect("lastStand")
        else:
            self.remove_multiplier_effect("lastStand")


    
    def gate_abilities(self):
        if self._vital_status['full_hp']:
            self.remove_active_ability("healSelf")
            self.remove_active_ability("leech")
        else:
            self.add_active_ability("healSelf")
            self.add_active_ability("leech")



    def attack(self, damage, selected_unit):
        



    def damage(self, attack):
        damage = attack - self._defence
        if damage <= 0:
            damage = 1
        self._health -= damage

    def true_damage(self, attack):
        self._health -= attack

    def venom_damage(self):
        max_damage = self._base_health * 0.15
        min_damage = self._base_health * 0.08
        venom = self._ability_data['active']['ticking']['venom']
        remaining_turns = 1 - (venom['ticks'] / venom['duration'])
        total_damage = min_damage + ((max_damage - min_damage) * remaining_turns)
        total_hp = self._health - total_damage
        if total_hp <= 0:
            self._health = 1
        else:
            self._health = total_hp



    def healSelf(self):
        if "weaken" in self._active_debuffs or "venom" in self._active_debuffs:
            self.remove_debuff("weaken")
            self.remove_debuff("venom")
        else:
            max_heal = self._base_health * 0.30
            min_heal = self._base_health * 0.01
            missing_hp = 1 - (self._health / self._base_health)
            total_heal = min_heal + ((max_heal - min_heal) * missing_hp)
            self.heal(total_heal)

    def heal(self, total_heal):
        total_hp = self._health + total_heal
        if total_hp >= self._base_health:
            self._health = self._base_health
            self.check_if_full_hp()
        else:
            self._health = total_hp



    def add_buff(self, ability):
        if ability not in self._active_buffs:
            self._active_buffs.append(ability)
            self.add_ticks(ability)
            self.add_multiplier_effect(ability)

    def add_debuff(self, ability):
        if ability not in self._active_debuffs:
            self._active_debuffs.append(ability)
            self.add_ticks(ability)
            self.add_multiplier_effect(ability)

    def add_ticks(self, ability):
        ticking = self._ability_data['active']['ticking']
        if ability in ticking:
            ticking[ability]['ticks'] = ticking[ability]['duration']

    def add_multiplier_effect(self, effect):
        match effect:
            case "enrage":
                self._multipliers[effect]['attack'] =   0.30
            case "harden":
                self._multipliers[effect]['defence'] =  0.40
            case "lastStand":
                self._multipliers[effect]['attack'] =   0.50
            case "pierce":
                self._multipliers[effect]['defence'] = -0.50
            case "weaken":
                self._multipliers[effect]['attack'] =  -0.30



    def remove_buff(self, ability):
        if ability in self._active_buffs:
            self._active_buffs.remove(ability)
            self.remove_ticks(ability)
            self.remove_multiplier_effect(ability)

    def remove_debuff(self, ability):
        if ability in self._active_debuffs:
            self._active_debuffs.remove(ability)
            self.remove_ticks(ability)
            self.remove_multiplier_effect(ability)
    
    def remove_ticks(self, ability):
        ticking = self._ability_data['active']['ticking']
        if ability in ticking:
            ticking[ability]['ticks'] = 0

    def remove_multiplier_effect(self, effect):
        match effect:
            case "enrage":
                self._multipliers[effect]['attack'] =  0
            case "harden":
                self._multipliers[effect]['defence'] = 0
            case "pierce":
                self._multipliers[effect]['defence'] = 0
            case "weaken":
                self._multipliers[effect]['attack'] =  0
            case "weaken":
                self._multipliers[effect]['attack'] =  0



    def add_active_ability(self, ability):
        if ability in self._abilities and ability not in self._active_abilities:
            self._active_abilities.append(ability)

    def remove_active_ability(self, ability):
        if ability in self._abilities and ability in self._active_abilities:
            self._active_abilities.remove(ability)