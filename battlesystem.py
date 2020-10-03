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
    run_msg = "Próbujesz uciec z walki z potworem " + name
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
    curr_hp = base_hp
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

    @staticmethod
    def print_monster_meet_options():
        print("Co robisz?")
        print("1) Zaczynasz walkę")
        print("2) Chcesz jej uniknąć")

    def try_to_run(self, monster: Monster) -> bool:
        print(monster.run_msg)
        if r.randint(0, 1) == 1:
            # Nie udało się uciec
            print("Udało ci się uciec!")
            if r.randint(0, 1) == 1:
                received_dmg = r.randint(1, self.curr_hp // 2)
                self.curr_hp -= received_dmg
                print("Niestety, otrzymujesz obrażenia w ilości", str(received_dmg), " i masz teraz", str(self.curr_hp),
                      "HP!")
            else:
                print("Na szczęście nie otrzymujesz żadnych obrażeń!")
            return True
        else:
            print("Ucieczka nie powiodła się!")
            return False

    def start_fight(self, monster: Monster):
        print("Rozpoczynasz walkę z " + monster.name)
        result = self.fight_with(monster)
        if result:
            print(monster.win_msg)
            return True
        else:
            print(monster.lose_msg)
            return False

    def on_monster_meet(self, monster: Monster) -> bool:
        print(monster.entry_msg)
        self.print_monster_meet_options()
        choice = int(input())
        if choice == 1:
            return self.start_fight(monster)
        elif self.try_to_run(monster):
            # TODO: Cofnij do poprzedniej lokalizacji
            print("Wracasz do lokalizacji ...")
            return True
        else:
            return self.start_fight(monster)
