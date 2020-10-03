from battlesystem import *


class Location:
    id = 0
    name = "Bagna"
    go_msg = "Możesz iść do lokalizacji o ID " + str(id)
    monster = None
    entry_msg = "Jesteś w " + name
    id_dst = []

    def __init__(self, id, name, go_msg, monster: Monster, entry_msg, id_dst):
        self.id = id
        self.name = name
        self.go_msg = go_msg
        self.monster = monster
        self.entry_msg = entry_msg
        self.id_dst = id_dst


Location(1, "Start", "Idź na start", None, "Jesteś na starcie", [2, 3]), Location(2, "Start", "Idź do lasu", None, "Jesteś w lesie", [1, 3, 4])