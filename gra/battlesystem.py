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
    run_msg = "Próbujesz uciec z walki z potworem " + name
    lose_msg = "Przegrywasz z potworem " + name
    win_msg = "Wygrywasz z potworem " + name

    def __init__(self, defense, dmg, hp, exp, name, entry_msg, lose_msg, win_msg, run_msg):
        self.defense = defense
        self.damage = dmg
        self.hp = hp
        self.exp = exp
        self.name = name
        self.entry_msg = entry_msg
        self.lose_msg = lose_msg
        self.win_msg = win_msg
        self.run_msg = run_msg