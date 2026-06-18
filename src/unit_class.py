

from millify import millify


class Unit:
    abilities = {
        "instant": {
            "attack": {},
            "healSelf": {},
            "leech": {},
        },
        "lingering": {
            "burn": {
                "display": "BRN", 
                "duration": 2,
                "state": 0
            },
            "enrage": {
                "display": "RGE", 
                "duration": 2,
                "state": 0
            },
            "harden": {
                "display": "HRD", 
                "duration": 2,
                "state": 0
            },
            "lastStand": {
                "display": "LST", 
            },
            "pierce": {
                "display": "PRC", 
                "duration": 4,
                "state": 0
            },
            "poison": {
                "display": "PSN", 
                "duration": 3,
                "state": 0
            },
            "regen": {
                "display": "RGN", 
                "duration": 3,
                "state": 0
            },
            "weaken": {
                "display": "WKN", 
                "duration": 3,
                "state": 0
            }
        }
    }


    def __init__(self, units_data, unit_idx=0, trait_idx=0):
        unit = units_data[unit_idx]
        unit_name = unit['name']
        trait = unit['traits'][trait_idx]
        trait_name = trait['name']
        health = trait['stats']['health']
        defence = trait['stats']['defence']
        attack = trait['stats']['attack']
        abilities = trait['abilities']


        if len(unit_name) < 1 or len(unit_name) > 13:
            raise ValueError("Invalid unit name length. Range: 1-13")
        self._unit = unit_name

        if len(trait_name) < 1 or len(trait_name) > 13:
            raise ValueError("Invalid trait name length. Range: 1-13")
        self._trait = trait_name


        if health < 1 or health > 9999999:
            raise ValueError("Invalid health value. Range: 1-9999999")
        self._base_health = health
        self._health = health

        if defence < 0 or defence > 999999:
            raise ValueError("Invalid defence value. Range: 0-999999")
        self._base_defence = defence
        self._defence = defence

        if attack < 0 or attack > 999999:
            raise ValueError("Invalid attack value. Range: 0-9999999")
        self._base_attack = attack
        self._attack = attack



        self._abilities = abilities
        self._active_buffs = []
        self._active_debuffs = []
        self._status = {
            "full_hp": True,
            "alive": True
        }

        self._burned_state = 0
        self._pierced_state = 0
        self._poisoned_state = 0
        self._weakened_state = 0
        self._enraged_state = 0
        self._hardened_state = 0
        self._regen_state = 0



    # Family and classification
    @property
    def unit(self):
        return self._unit.title()
    @property
    def trait(self):
        return self._trait.title()



    # Base and current health
    @property
    def base_health(self):
        return millify(self._base_health, precision=1)
    @property
    def health(self):
        return millify(self._health, precision=1)



    # Base and current defence
    @property
    def base_defence(self):
        return self._base_defence
    @property
    def defence(self):
        return round(self._defence, 1)



    # Base and current attack damage
    @property
    def base_attack(self):
        return self._base_attack
    @property
    def attack(self):
        return round(self._attack, 1)



    # List of abilities
    @property
    def abilities(self):
        return sorted([ability for ability in self._abilities if ability and ability != "lastStand"])



    def can(self, ability):
        if ability in self._abilities:
            return True
        return False



    def show_buffs(self):
        statuses = []
        for buff in self._active_buffs:
            statuses.append(Unit.abilities['lingering'][buff]['display'])
        return self.compile_statuses(statuses)

    def show_debuffs(self):
        statuses = []
        for debuff in self._active_debuffs:
            statuses.append(Unit.abilities['lingering'][debuff]['display'])
        return self.compile_statuses(statuses)

    def compile_statuses(self, statuses):
        status_message = ""
        if statuses:
            for status in statuses:
                if status_message:
                    status_message += "|"
                status_message += status
        return status_message



    def check_general_status(self):
        self.check_is_alive()
        self.check_is_full_hp()
        self.check_is_lastStand()

    def check_applied_status(self):
        self.check_is_burned()
        self.check_is_enraged()
        self.check_is_hardened()
        self.check_is_pierced()
        self.check_is_poisoned()
        self.check_is_regen()
        self.check_is_weakened()



    def check_is_alive(self):
        if self._health <= 0:
            self._status['alive'] = False

    def check_is_full_hp(self):
        if self._health == self._base_health:
            self._status['full_hp'] = True
        else:
            self._status['full_hp'] = False
            self.remove_status("healSelf")



    def damage(self, attack):
        damage = attack - self._defence
        if damage <= 0:
            damage = 1
        self._health -= damage
        self.check_is_alive()

    def true_damage(self, attack):
        self._health -= attack
        self.check_is_alive()



    def burn(self):
        ability = "burn"
        self.add_debuff(ability)

    def check_is_burned(self):
        if self._burned_state > 0:
            self._burned_state -= 1
            self.damage(self._base_health * 0.30)
        if self._burned_state == 0:
            self.remove_debuff("burn")



    def pierce(self):
        ability = "pierce"
        self.add_debuff(ability)
        self._defence = self._base_defence - (self._base_defence * 0.50)

    def check_is_pierced(self):
        if self._pierced_state > 0:
            self._pierced_state -= 1
        if self._pierced_state == 0:
            self.remove_debuff("pierce")
            self._defence = self._base_defence
            


    def poison(self):
        ability = "poison"
        self.add_debuff(ability)

    def check_is_poisoned(self):
        if self._poisoned_state > 0:
            self._poisoned_state -= 1
            self.poison_damage()
        if self._poisoned_state == 0:
            self.remove_debuff("poison")

    def poison_damage(self):
        max_damage = self._base_health * 0.15
        min_damage = self._base_health * 0.08
        remaining_turns = 1 - (self._poisoned_state / Unit.poison_duration)
        total_damage = min_damage + ((max_damage - min_damage) * remaining_turns)
        total_hp = self._health - total_damage
        if total_hp <= 0:
            self._health = 1
        else:
            self._health = total_hp



    def weaken(self):
        ability = "weaken"
        self.add_debuff(ability)
        self._attack = self._base_attack - (self._base_attack * 0.30)

    def check_is_weakened(self):
        if self._weakened_state > 0:
            self._weakened_state -= 1
        if self._weakened_state == 0:
            self.remove_debuff("weaken")
            self._attack = self._base_attack



    def enrage(self):
        ability = "enrage"
        self.add_buff(ability)
        self._attack = self._base_attack + (self._base_attack * 0.30)

    def check_is_enraged(self):
        if self._enraged_state > 0:
            self._enraged_state -= 1
        if self._enraged_state == 0:
            self.remove_buff("enrage")
            self._attack = self._base_attack



    def harden(self):
        ability = "harden"
        self.add_buff(ability)
        self._defence = self._base_defence + (self._base_defence * 0.40)

    def check_is_hardened(self):
        if self._hardened_state > 0:
            self._hardened_state -= 1
        if self._hardened_state == 0:
            self.remove_buff("harden")
            self._defence = self._base_defence



    def heal_self(self):
        if "weaken" in self._active_debuffs or "poison" in self._active_debuffs:
            self.remove_debuff("weaken")
            self.remove_debuff("poison")
            self._weakened_state = 0
            self._poisoned_state = 0
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
            self.check_is_full_hp()
        else:
            self._health = total_hp



    def check_is_lastStand(self):
        if self.can("lastStand"):
            if self._health < self._base_health * 0.30:
                self._attack = self._base_attack + (self._base_attack * 0.50)
            else:
                self._attack = self._base_attack



    def regen(self):
        ability = "regen"
        self.add_buff(ability)

    def check_is_regen(self):
        if self._regen_state > 0:
            self._regen_state -= 1
            self.heal(self._base_health * 0.10)
        elif self._regen_state == 0:
            self.remove_buff("regen")



    def add_buff(self, ability):
        if ability not in self._active_buffs:
            self._active_buffs.append(ability)
            self.add_state(ability)

    def add_debuff(self, ability):
        if ability not in self._active_debuffs:
            self._active_debuffs.append(ability)
            self.add_state(ability)

    def add_state(self, ability):
        if "state" in Unit.abilities['lingering'][ability].keys():
            Unit.abilities['lingering'][ability]['state'] = Unit.abilities['lingering'][ability]['duration']



    def remove_buff(self, ability):
        if ability in self._active_buffs:
            self._active_buffs.remove(ability)
            self.remove_state(ability)

    def remove_debuff(self, ability):
        if ability in self._active_debuffs:
            self._active_debuffs.remove(ability)
            self.remove_state(ability)
    
    def remove_state(self, ability):
        if "state" in Unit.abilities['lingering'][ability].keys():
            Unit.abilities['lingering'][ability]['state'] = 0