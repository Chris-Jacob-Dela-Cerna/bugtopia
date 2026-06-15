

from millify import millify


class Unit:
    burn_duration = 2
    pierce_duration = 4
    poison_duration = 3
    weaken_duration = 3

    enrage_duration = 2
    harden_duration = 2
    regen_duration = 3


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


        self._can_attack = False
        self._can_burn = False
        self._can_leech = False
        self._can_pierce = False
        self._can_poison = False
        self._can_weaken = False

        self._can_enrage = False
        self._can_harden = False
        self._can_healSelf = False
        self._can_regen = False

        self._can_lastStand = False


        if "attack" in abilities:
            self._can_attack = True
        if "burn" in abilities:
            self._can_burn = True
        if "leech" in abilities:
            self._can_leech = True
        if "pierce" in abilities:
            self._can_pierce = True
        if "poison" in abilities:
            self._can_poison = True
        if "weaken" in abilities:
            self._can_weaken = True

        if "enrage" in abilities:
            self._can_enrage = True
        if "harden" in abilities:
            self._can_harden = True
        if "healSelf" in abilities:
            self._can_healSelf = True
        if "lastStand" in abilities:
            self._can_lastStand = True
        if "regen" in abilities:
            self._can_regen = True


        self._is_alive = True
        self._is_full_hp = False

        self._is_burned = False
        self._burned_state = 0
        self._is_pierced = False
        self._pierced_state = 0
        self._is_poisoned = False
        self._poisoned_state = 0
        self._is_weakened = False
        self._weakened_state = 0

        self._is_enraged = False
        self._enraged_state = 0
        self._is_hardened = False
        self._hardened_state = 0
        self._is_regen = False
        self._regen_state = 0

        self._is_lastStand = False



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



    # Inflicting Abilities - Instant
    @property
    def can_attack(self):
        return self._can_attack
    @property
    def can_leech(self):
        return self._can_leech

    # Inflicting Abilities - With Duration
    @property
    def can_burn(self):
        return self._can_burn
    @property
    def can_pierce(self):
        return self._can_pierce
    @property
    def can_poison(self):
        return self._can_poison
    @property
    def can_weaken(self):
        return self._can_weaken


    # Self Abilities - Instant
    @property
    def can_healSelf(self):
        return self._can_healSelf

    # Self Abilities - With Duration
    @property
    def can_enrage(self):
        return self._can_enrage
    @property
    def can_harden(self):
        return self._can_harden
    @property
    def can_regen(self):
        return self._can_regen


    # Passive Abilities
    @property
    def can_lastStand(self):
        return self._can_lastStand



    # General Status
    @property
    def is_alive(self):
        return self._is_alive
    @property
    def is_full_hp(self):
        return self._is_full_hp

    # Debuff Status
    @property
    def is_burned(self):
        return self._is_burned
    @property
    def is_pierced(self):
        return self._is_pierced
    @property
    def is_poisoned(self):
        return self._is_poisoned
    @property
    def is_weakened(self):
        return self._is_weakened

    # Buff Status
    @property
    def is_enraged(self):
        return self._is_enraged
    @property
    def is_hardened(self):
        return self._is_hardened
    @property
    def is_regen(self):
        return self._is_regen 

    # Triggered Status
    @property
    def is_lastStand(self):
        return self._is_lastStand



    def show_debuffs(self):
        statuses = []
        if self._is_burned:
            statuses.append("BRN")
        if self._is_pierced:
            statuses.append("PRC")
        if self._is_poisoned:
            statuses.append("PSN")
        if self._is_weakened:
            statuses.append("WKN")
        return self.compile_statuses(statuses)

    def show_buffs(self):
        statuses = []
        if self._is_enraged:
            statuses.append("RGE")
        if self._is_hardened:
            statuses.append("HRD")
        if self._is_lastStand:
            statuses.append("LSD")
        if self._is_regen:
            statuses.append("RGN")
        return self.compile_statuses(statuses)



    def check_general_status(self):
        self.check_is_alive()
        self.check_is_full_hp()

    def check_applied_status(self):
        self.check_is_pierced()
        self.check_is_poisoned()



    def check_is_alive(self):
        if self._health <= 0:
            self._is_alive = False
            self._health = 0

    def check_is_full_hp(self):
        if self._health == self._base_health:
            self._is_full_hp = False
        else:
            self._is_full_hp = True



    def damage(self, attack):
        residual_damage = attack - self._defence
        if residual_damage <= 0:
            residual_damage = 1
        self._health -= residual_damage
        self.check_is_alive()


    def burn(self):
        self._is_burned = True
        self._burned_state = Unit.burn_duration

    def check_is_burned(self):
        if self._burned_state > 0:
            self._burned_state -= 1
            self.damage(self._base_health * 0.30)
        if self._burned_state == 0:
            self._is_burned = False


    def pierce(self):
        self._is_pierced = True
        self._pierced_state = Unit.pierce_duration
        self._defence = self._base_defence - (self._base_defence * 0.50)

    def check_is_pierced(self):
        if self._pierced_state > 0:
            self._pierced_state -= 1
        if self._pierced_state == 0:
            self._is_pierced = False
            self._defence = self._base_defence


    def poison(self):
        self._is_poisoned = True
        self._poisoned_state = Unit.poison_duration

    def check_is_poisoned(self):
        if self._poisoned_state > 0:
            self._poisoned_state -= 1
            self.poison_damage()
        if self._poisoned_state == 0:
            self._is_poisoned = False

    def poison_damage(self):
        max_damage = self._base_health * 0.25
        min_damage = self._base_health * 0.15
        remaining_turns = 1 - (self._poison_state / Unit.poison_duration)

        total_damage = min_damage + ((max_damage - min_damage) * remaining_turns)
        total_hp = self._health - total_damage

        if total_hp <= 0:
            self._health = 1
        else:
            self._health = total_hp


    def weaken(self):
        self._is_weakened = True
        self._weakened_state = Unit.weaken_duration
        self._attack = self._base_attack - (self._base_attack * 0.30)

    def check_is_weakened(self):
        if self._weakened_state > 0:
            self._weakened_state -= 1
        if self._weakened_state == 0:
            self._is_weakened = False
            self._attack = self._base_attack



    def enrage(self):
        self._is_enraged = True
        self._enraged_state = Unit.enrage_duration
        self._attack = self._base_attack + (self._base_attack * 0.30)

    def check_is_enraged(self):
        if self._enraged_state > 0:
            self._enraged_state -= 1
        if self._enraged_state == 0:
            self._is_enraged = False
            self._attack = self._base_attack


    def harden(self):
        self._is_hardened = True
        self._hardened_state = Unit.harden_duration
        self._defence = self._base_defence + (self._base_defence * 0.40)

    def check_is_hardened(self):
        if self._hardened_state > 0:
            self._hardened_state -= 1
        if self._hardened_state == 0:
            self._is_hardened = False
            self._defence = self._base_defence


    def heal_self(self):
        max_heal = self._base_health * 0.30
        min_heal = self._base_health * 0.01
        missing_hp = 1 - (self._health / self._base_health)

        total_heal = min_heal + ((max_heal - min_heal) * missing_hp)
        self.heal(total_heal)
    

    def regen(self):
        self._is_regen = True
        self._regen_state = Unit.regen_duration

    def check_is_regen(self):
        if self._regen_state > 0:
            self._regen_state -= 1
            self.heal(self._base_health * 0.10)
        if self._regen_state == 0:
            self._is_regen = False



    def heal(self, total_heal):
        total_hp = self._health + total_heal
        if total_hp >= self._base_health:
            self._health = self._base_health
            self.check_is_full_hp()
        else:
            self._health = total_hp



    def compile_statuses(statuses):
        status_message = ""
        if bool(statuses):
            for status in statuses:
                if bool(status_message):
                    status_message += "|"
                status_message += status
        else:
            status_message += "None"
        return status_message