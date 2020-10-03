import random as r


class Weapon:
    name = "Broń"
    damage = 0
    luck = 1.0

    def __init__(self, name, dmg, luck):
        self.name = name
        self.damage = dmg
        self.luck = luck


# class MonsterAttack:
#     damage_modifier = 0
#
#     def __init__(self, dmg_mod):
#         self.damage_modifier = dmg_mod
#

class Monster:
    defense = 0
    damage = 0
    hp = 100
    exp = 10
    name = "Potwór"
    entry_msg = "Spotykasz potwora " + name
    run_msg = "Próbujesz uciec z walkis od potwora " + name
    lose_msg = "Przegrywasz z potworem " + name
    win_msg = "Wygrywasz z potworem " + name

    def __init__(self, attack, defense, dmg, hp, exp, name, entry_msg, lose_msg, win_msg, run_msg):
        self.attack = attack
        self.defense = defense
        self.damage = dmg
        self.hp = hp
        self.exp = exp
        self.name = name
        self.entry_msg = entry_msg
        self.lose_msg = lose_msg
        self.win_msg = win_msg
        self.run_msg = run_msg


class Player:
    base_hp = 50
    defense = 0.8
    points = 0
    weapon = Weapon("Hand", 5, 1.0)

    def pickup_weapon(self, new_weapon: Weapon):
        self.weapon = new_weapon
        print("Podniosłeś broń " + new_weapon.name)

    def calc_max_damage(self, opponent: Monster):
        return self.weapon.damage * opponent.defense

    def fight_with(self, monster: Monster) -> bool:
        """
        Simulates a fight with given monster
        :rtype: true if player won, false otherwise
        """
        # Max monster attack damage
        max_mon_dmg = monster.damage * self.defense
        # Max player attack damage
        max_player_dmg = self.calc_max_damage(monster)
        player_hp = self.base_hp
        monster_hp = monster.hp

        player_moves = 0
        monster_moves = 0
        while player_hp > 0:
            player_dmg_mod = min(r.random() + 0.5, 1.0)
            monster_hp -= player_dmg_mod * max_player_dmg
            player_moves += 1

        while monster_hp > 0:
            mon_dmg_mod = min(r.random() + 0.3, 1.0)
            player_hp -= mon_dmg_mod * max_mon_dmg
            monster_moves += 1

        result = player_moves >= monster_moves
        if result:
            self.points += self.weapon.luck * monster.exp
        return result
