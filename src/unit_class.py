

from millify import millify


class Unit:
    poison_duration = 3 * 2
    pierce_duration = 4 * 2
    
    def __init__(self, unit_idx, trait_idx, units_data):
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
        if defence < 0 or defence > 9999999:
            raise ValueError("Invalid defence value. Range: 0-9999999")
        self._base_defence = defence
        self._defence = defence

        attack = trait['stats']['attack']
        if attack < 0 or attack > 9999999:
            raise ValueError("Invalid attack value. Range: 0-9999999")
        self._attack = attack

        abilities = trait['abilities']
        self._can_attack = False
        if "attack" in abilities:
            self._can_attack = True
        self._can_healSelf = False
        if "healSelf" in abilities:
            self._can_healSelf = True
        self._can_poison = False
        if "poison" in abilities:
            self._can_poison = True
        self._can_pierce = False
        if "pierce" in abilities:
            self._can_pierce = True

        self._is_alive = True
        self._is_full_hp = False

        self._is_poisoned = False
        self._poison_state = 0

        self._is_pierced = False
        self._pierced_state = 0


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
        return self._defence

    @property
    def attack(self):
        return self._attack
    
    @property
    def can_attack(self):
        return self._can_attack
    
    @property
    def can_healSelf(self):
        return self._can_healSelf

    @property
    def can_poison(self):
        return self._can_poison

    @property
    def can_pierce(self):
        return self._can_pierce
    
    @property
    def is_alive(self):
        return self._is_alive

    @property
    def is_full_hp(self):
        return self._is_full_hp
    
    @property
    def is_poisoned(self):
        return self._is_poisoned

    @property
    def is_pierced(self):
        return self._is_pierced
    
    def status(self):
        statuses = []
        if self._is_poisoned:
            statuses.append("PSN")
        if self._is_pierced:
            statuses.append("PRC")
        status_message = ""
        if bool(statuses):
            for status in statuses:
                if bool(status_message):
                    status_message += "|"
                status_message += status
        return status_message

    def check_is_alive(self):
        if self._health <= 0:
            self._is_alive = False
            self._health = 0

    def damage(self, attack):
        residual_damage = attack - self._defence
        if residual_damage <= 0:
            residual_damage = 1
        self._health -= residual_damage
        self.check_is_alive()


    def check_is_full_hp(self):
        if self._health == self._base_health:
            self._is_full_hp = False
        else:
            self._is_full_hp = True

    def heal(self):
        max_heal = self._base_health / 3.3
        min_heal = self._base_health / 100
        missing_hp = 1 - (self._health / self._base_health)

        total_heal = min_heal + ((max_heal - min_heal) * missing_hp)
        total_hp = self._health + total_heal

        if total_hp >= self._base_health:
            self._health = self._base_health
            self.check_is_full_hp()
        else:
            self._health = total_hp


    def poison(self):
        self._is_poisoned = True
        self._poison_state = Unit.poison_duration

    def check_is_poisoned(self):
        if self._poison_state > 0:
            self._poison_state -= 1
            self.poison_damage()
        else:
            self._is_poisoned = False

    def poison_damage(self):
        max_damage = self._base_health / 4
        min_damage = self._base_health / 6.6
        remaining_turns = 1 - (self._poison_state / Unit.poison_duration)

        total_damage = min_damage + ((max_damage - min_damage) * remaining_turns)
        total_hp = self._health - total_damage

        if total_hp <= 0:
            self._health = 1
        else:
            self._health = total_hp


    def pierce(self):
        self._is_pierced = True
        self._pierced_state = Unit.pierce_duration
        self._defence = self._base_defence / 2

    def check_is_pierced(self):
        if self._pierced_state > 0:
            self._pierced_state -= 1
        else:
            self._is_pierced = False
            self._defence = self._base_defence