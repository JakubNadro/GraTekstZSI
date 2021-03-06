import random as r
import string

from gra.battlesystem import *


class Location:
    id = 0
    name = "Lokalizacja"
    go_msg = "Możesz iść do lokalizacji o ID " + str(id)
    monster = None
    entry_msg = "Jesteś w " + name
    id_dst = []

    def __init__(self, id: int, name: string, go_msg: string, monster: Monster, entry_msg: string, id_dst: list):
        self.id = id
        self.name = name
        if go_msg is None:
            self.go_msg = "Idź do " + self.name
        else:
            self.go_msg = go_msg
        self.monster = monster
        self.entry_msg = entry_msg
        self.id_dst = id_dst


class Player:
    base_hp = 80
    curr_hp = base_hp
    defense = 0.75
    points = 0
    weapon = Weapon("Wirusowy Miecz (special power: szansa na zarażenie przeciwnika stojącego w promieniu 2m)", 30, 1.1)

    def pickup_weapon(self, new_weapon: Weapon):
        self.weapon = new_weapon
        print("Podniosłeś broń " + new_weapon.name)

    def regenerate_hp(self, amount: int):
        if amount == 0:
            return
        self.curr_hp += max(0, amount)
        self.curr_hp = min(self.base_hp, self.curr_hp)
        print("Zregenerowałeś {0} HP! Twoje obecne zdrowie: {1}/{2}".format(amount, round(self.curr_hp, 2),
                                                                            round(self.base_hp, 2)))

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
        monster_hp = monster.hp

        moves = 0

        while self.curr_hp > 0 and monster_hp > 0:
            mon_dmg_mod = min(r.random() + 0.3, 1.0)
            self.curr_hp -= mon_dmg_mod * max_mon_dmg
            # print("Monster_HP:", monster_hp)
            player_dmg_mod = min(r.random() + 0.5, 1.0)
            monster_hp -= player_dmg_mod * max_player_dmg
            moves += 1

        result = self.curr_hp > monster_hp
        if result:
            self.points += self.weapon.luck * monster.exp
        return result

    @staticmethod
    def print_monster_meet_options():
        print("Co robisz?")
        print("1) Rozpoczynasz walkę")
        print("2) Chcesz jej uniknąć")
        print("Wszystko inne) Rozpoczynasz walkę")

    def try_to_run(self, monster: Monster) -> bool:
        print("Walka:", monster.run_msg)
        if r.randint(0, 1) == 1:
            # Nie udało się uciec
            print("Walka: Udało ci się uciec!")
            if r.randint(0, 1) == 1:
                received_dmg = r.randint(1, self.curr_hp // 2)
                self.curr_hp -= received_dmg
                print("Walka: Niestety, otrzymujesz obrażenia w ilości", str(received_dmg), "i masz teraz",
                      str(self.curr_hp),
                      "HP!")
            else:
                print("Walka: Na szczęście nie otrzymujesz żadnych obrażeń!")
            return True
        else:
            print("Walka: Ucieczka nie powiodła się!")
            return False

    def start_fight(self, monster: Monster):
        print("Walka: Rozpoczynasz walkę z", monster.name)
        result = self.fight_with(monster)
        # print("Result:", result)
        if result:
            monster.defeated = True
            print(monster.win_msg)
            print("HP:", round(self.curr_hp, 2), " / ", round(self.base_hp, 2))
            print("Punkty:", round(self.points, 2))
            return True
        else:
            print(monster.lose_msg)
            return False

    def on_monster_meet(self, monster: Monster) -> bool:
        print(monster.entry_msg)
        self.print_monster_meet_options()
        # Accept only numeric values
        choice = ""
        while not choice.isnumeric():
            choice = input("Walka:")

        if choice == 2 and self.try_to_run(monster):
            # Fix circular inputs
            from gra.locationsystem import get_previous_location, move

            prev_loc = get_previous_location()

            if prev_loc is not None:
                print("Walka: Wracasz do lokalizacji", prev_loc.name)
                move(self, prev_loc.id)
            else:
                print("Walka: Nie masz gdzie uciec!")
                return False
            return True
        else:
            return self.start_fight(monster)


class GameManager:

    def __init__(self):
        self.player = Player()
