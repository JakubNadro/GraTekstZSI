import string

from gra.battlesystem import *


class Location:
    id = 0
    name = "Bagna"
    go_msg = "Możesz iść do lokalizacji o ID " + str(id)
    monster = None
    entry_msg = "Jesteś w " + name
    id_dst = []

    def __init__(self, id: int, name: string, go_msg: string, monster: Monster, entry_msg: string, id_dst: list):
        self.id = id
        self.name = name
        self.go_msg = go_msg
        self.monster = monster
        self.entry_msg = entry_msg
        self.id_dst = id_dst
