from gra.game import Location, GameManager
from gra.battlesystem import Monster
from gra.ui import quit_game

stack = [
    1
]


def szukanie(droga):
    # Fix circular inputs
    from gra.config import locations

    for i in range(0, len(locations)):
        if locations[i]['id'] == droga:
            return locations[i]


def get_curr_location() -> Location:
    return szukanie(stack.top())


def get_previous_location() -> Location:
    curr_location = stack.top()
    stack.pop()
    prev_location = szukanie(stack.top())
    stack.append(curr_location)
    return prev_location


def move(game_mgr: GameManager, droga):
    stack.append(droga)
    currloc = get_curr_location()
    print(currloc.entry_msg)
    if currloc.monster != None:
        enemy = Monster
        print(enemy.entry_msg)
        is_alive = game_mgr.player.on_monster_meet(currloc.monster)
        if is_alive == True:
            print("Brawo!!! Pokonałeś potwora \n" + currloc.go_msg)
        else:
            quit_game(game_mgr)
