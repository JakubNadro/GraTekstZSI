from gra.game import Location, GameManager
from gra.battlesystem import Monster

stack = [
    1
]


def szukanie(droga):
    # Fix circular inputs
    from gra.config import locations

    for i in range(0, len(locations)):
        if locations[i].id == droga:
            return locations[i]


def get_curr_location() -> Location:
    return szukanie(stack[len(stack) - 1])


def get_previous_location() -> Location:
    index = len(stack) - 2
    # Nie chcemy wyjsc na ujemne indexy
    if index < 0:
        return None
    return szukanie(stack[index])


def move(game_mgr: GameManager, droga):
    stack.append(droga)
    currloc = get_curr_location()
    print(currloc.entry_msg)

    if currloc.monster != None:
        is_alive = game_mgr.player.on_monster_meet(currloc.monster)
        if is_alive:
            print("Brawo!!! Pokonałeś potwora \n" + currloc.go_msg)
            possible_locations()
        else:
            from gra.ui import quit_game

            quit_game(game_mgr)


def possible_locations():
    print("Lokalizacja:", get_curr_location().name)
    from gra.config import locations

    curr_possibs = get_curr_location().id_dst
    for i in range(0, len(locations)):
        if locations[i].id in curr_possibs:
            print(str(locations[i].id) + ")", locations[i].go_msg)
