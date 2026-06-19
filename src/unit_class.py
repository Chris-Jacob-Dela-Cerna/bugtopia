

from millify import millify


class Unit:
    ability_data = {
        "active": {
            "instant": {
                "attack":   {},
                "healSelf": {},
                "leech":    {},
            },
            "ticking": {
                "burn":     {"display": "BRN", "duration": 2, "ticks": 0},
                "enrage":   {"display": "RGE", "duration": 2, "ticks": 0},
                "harden":   {"display": "HRD", "duration": 2, "ticks": 0},
                "pierce":   {"display": "PRC", "duration": 4, "ticks": 0},
                "poison":   {"display": "PSN", "duration": 3, "ticks": 0},
                "regen":    {"display": "RGN", "duration": 3, "ticks": 0},
                "weaken":   {"display": "WKN", "duration": 3, "ticks": 0}
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
        "poison":     {"health": 0, "defence": 0, "attack": 0},
        "regen":      {"health": 0, "defence": 0, "attack": 0},
        "weaken":     {"health": 0, "defence": 0, "attack": 0}
    }

    def __init__(self, units_data, unit_idx=0, trait_idx=0):
        unit = units_data[unit_idx]
        unit_name = unit['name']
        if len(unit_name) < 1 or len(unit_name) > 13:
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
        self._base_health = health
        self._health = health


        defence = trait['stats']['defence']
        if defence < 0 or defence > 999999:
            raise ValueError("Invalid defence value. Range: 0-999999")
        self._base_defence = defence
        self._defence = defence


        attack = trait['stats']['attack']
        if attack < 0 or attack > 999999:
            raise ValueError("Invalid attack value. Range: 0-9999999")
        self._base_attack = attack
        self._attack = attack


        abilities = trait['abilities']
        self._abilities = abilities

        actives = Unit.ability_data['active']
        self._active_abilities = [ability for ability in abilities if ability in actives['instant'] or ability in actives['ticking']]
        self._passive_abilities = [ability for ability in abilities if ability in Unit.ability_data['passive']]

        self._active_buffs = []
        self._active_debuffs = []
        self._vital_status = {
            "full_hp": True,
            "alive": True
        }



    @property
    def unit(self):
        return self._unit.title()
    @property
    def trait(self):
        return self._trait.title()



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
        for ability in Unit.multipliers.keys():
            if ability['defence']:
                base_multiplier += ability['defence']
        defence = self._defence * base_multiplier
        return round(defence, 1)



    @property
    def base_attack(self):
        return self._base_attack
    @property
    def attack(self):
        base_multiplier = 1.00
        for ability in Unit.multipliers.keys():
            if ability['attack']:
                base_multiplier += ability['attack']
        attack = self._attack * base_multiplier
        return round(attack, 1)



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
            statuses.append(Unit.ability_data['ticking'][buff]['display'])
        return self.compile_statuses(statuses)

    def show_debuffs(self):
        statuses = []
        for debuff in self._active_debuffs:
            statuses.append(Unit.ability_data['ticking'][debuff]['display'])
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



    def check_vital_status(self):
        self.check_if_alive()
        self.check_if_full_hp()

    def check_applied_effects(self):
        self.check_if_burned()
        self.check_if_enraged()
        self.check_if_hardened()
        self.check_if_pierced()
        self.check_if_poisoned()
        self.check_if_regen()
        self.check_if_weakened()

    def check_passives(self):
        self.check_if_lastStand()



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



    def damage(self, attack):
        damage = attack - self._defence
        if damage <= 0:
            damage = 1
        self._health -= damage

    def true_damage(self, attack):
        self._health -= attack


    def check_effects(self):
        for effect in self.active_buffs:
            self.apply_effect(effect)
            self.tick_effect(effect, "buff")
        for effect in self.active_buffs:
            self.apply_effect(effect)
            self.tick_effect(effect, "debuff")

    def apply_effect(self, effect):
        match effect:
            case "burn":
                self.damage(self._base_health * 0.30)
            case "enrage":
                Unit.multipliers[effect]['attack'] = 0.30
            case "harden":
                Unit.multipliers[effect]['defence'] = 0.40
            case "pierce":
                Unit.multipliers[effect]['defence'] = -0.50
            case "poison":
                self.poison_damage()
            case "regen":
                self.heal(self._base_health * 0.10)
            case "weaken":
                Unit.multipliers[effect]['attack'] = -0.30

    def tick_effect(self, ability, effect_type):
        ticks = Unit.ability_data['active']['ticking'][ability]['ticks']
        if ticks > 0:
            ticks -= 1
        if ticks == 0:
            if effect_type == "buff":
                self.remove_buff(ability)
            elif effect_type == "debuff":
                self.remove_debuff(ability)





    def burn(self):
        ability = "burn"
        self.add_debuff(ability)

    def check_if_burned(self):
        ability = "burn"
        ticks = Unit.ability_data['active']['ticking'][ability]['ticks']
        if ticks > 0:
            ticks -= 1
            self.damage(self._base_health * 0.30)
        elif ticks == 0:
            self.remove_debuff(ability)



    def pierce(self):
        ability = "pierce"
        self.add_debuff(ability)
        Unit.multipliers[ability]['defence'] = -0.50

    def check_if_pierced(self):
        ability = "pierce"
        ticks = Unit.ability_data['active']['ticking'][ability]['ticks']
        if ticks > 0:
            ticks -= 1
        elif ticks == 0:
            self.remove_debuff(ability)
            Unit.multipliers[ability]['defence'] = 0



    def poison(self):
        ability = "poison"
        self.add_debuff(ability)

    def check_if_poisoned(self):
        ability = "poison"
        ticks = Unit.ability_data['active']['ticking'][ability]['ticks']
        if ticks > 0:
            ticks -= 1
            self.poison_damage()
        elif ticks == 0:
            self.remove_debuff(ability)

    def poison_damage(self):
        max_damage = self._base_health * 0.15
        min_damage = self._base_health * 0.08
        poison = Unit.ability_data['active']['poison']
        remaining_turns = 1 - (poison['ticks'] / poison['duration'])
        total_damage = min_damage + ((max_damage - min_damage) * remaining_turns)
        total_hp = self._health - total_damage
        if total_hp <= 0:
            self._health = 1
        else:
            self._health = total_hp



    def weaken(self):
        ability = "weaken"
        self.add_debuff(ability)
        Unit.multipliers[ability]['attack'] = -0.30

    def check_if_weakened(self):
        ability = "weaken"
        ticks = Unit.ability_data['active']['ticking'][ability]['ticks']
        if ticks > 0:
            ticks -= 1
        elif ticks == 0:
            self.remove_debuff(ability)
            Unit.multipliers[ability]['attack'] = 0



    def enrage(self):
        ability = "enrage"
        self.add_buff(ability)
        Unit.multipliers[ability]['attack'] = 0.30

    def check_if_enraged(self):
        ability = "enrage"
        ticks = Unit.ability_data['active']['ticking'][ability]['ticks']
        if ticks > 0:
            ticks -= 1
        elif ticks == 0:
            self.remove_buff(ability)
            Unit.multipliers[ability]['attack'] = 0



    def harden(self):
        ability = "harden"
        self.add_buff(ability)
        Unit.multipliers[ability]['defence'] = 0.40

    def check_if_hardened(self):
        ability = "harden"
        ticks = Unit.ability_data['active']['ticking'][ability]['ticks']
        if ticks > 0:
            ticks -= 1
        elif ticks == 0:
            self.remove_buff(ability)
            Unit.multipliers[ability]['defence'] = 0



    def healSelf(self):
        if "weaken" in self._active_debuffs or "poison" in self._active_debuffs:
            self.remove_debuff("weaken")
            self.remove_debuff("poison")
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



    def check_if_lastStand(self):
        if self.can("lastStand"):
            if self._health < self._base_health * 0.30:
                self._attack = self._base_attack + (self._base_attack * 0.50)
            else:
                self._attack = self._base_attack



    def regen(self):
        ability = "regen"
        self.add_buff(ability)

    def check_if_regen(self):
        ability = "regen"
        ticks = Unit.ability_data['active']['ticking'][ability]['ticks']
        if ticks > 0:
            ticks -= 1
            self.heal(self._base_health * 0.10)
        elif ticks == 0:
            self.remove_buff(ability)



    def add_buff(self, ability):
        if ability not in self._active_buffs:
            self._active_buffs.append(ability)
            self.add_ticks(ability)

    def add_debuff(self, ability):
        if ability not in self._active_debuffs:
            self._active_debuffs.append(ability)
            self.add_ticks(ability)

    def add_ticks(self, ability):
        ticking = Unit.ability_data['active']['ticking']
        if ability in ticking:
            ticking[ability]['ticks'] = ticking[ability]['duration']



    def remove_buff(self, ability):
        if ability in self._active_buffs:
            self._active_buffs.remove(ability)
            self.remove_ticks(ability)

    def remove_debuff(self, ability):
        if ability in self._active_debuffs:
            self._active_debuffs.remove(ability)
            self.remove_ticks(ability)
    
    def remove_ticks(self, ability):
        ticking = Unit.ability_data['active']['ticking']
        if ability in ticking:
            ticking[ability]['ticks'] = 0



    def add_active_ability(self, ability):
        if ability in self._abilities and ability not in self._active_abilities:
            self._active_abilities.append(ability)

    def remove_active_ability(self, ability):
        if ability in self._abilities and ability in self._active_abilities:
            self._active_abilities.remove(ability)