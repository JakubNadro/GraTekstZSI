from gra.game import GameManager
from gra.locationsystem import *


def quit_game(game_mgr: None):
    global running
    running = False
    print("Zamykanie gry...")


def game_help(game_mgr: GameManager):
    print("--- Dostępne polecenia ---")
    for cmd in cmds:
        print(cmd, "-", cmds_desc[cmd])
    print("--------------------------")


def game_info(game_mgr):
    print("--- Informacje o graczu ---")
    print("HP:", round(game_mgr.player.curr_hp, 2), " / ", round(game_mgr.player.base_hp, 2))
    print("Punkty:", round(game_mgr.player.points, 2))
    print("Broń:", game_mgr.player.weapon)
    print("---------------------------")


def game_pwd(game_mgr):
    print("Jesteś teraz w", get_curr_location().name)


cmds = {
    "quit": quit_game,
    "help": game_help,
    "info": game_info,
    "pwd": game_pwd
}

cmds_desc = {
    "help": "Wyświetla okienko pomocy",
    "quit": "Zamyka grę",
    "info": "Wyświetla informacje o graczu",
    "pwd": "Wyświetla obecną lokalizację"
}

running: bool = True


def main_loop(game_mgr):
    while running:
        if game_mgr.player.points >= 500:
            print("\n\nBrawo! Przeszedłes grę! Uzyskałes ponad 500 punktów!")
            quit_game(game_mgr)
            break

        cmd = input(":")

        if cmd in cmds:
            cmds[cmd](game_mgr)
        elif cmd.isnumeric():
            cmd = int(cmd)

            # When stack size = 1 previous location does not exist
            if cmd not in get_curr_location().id_dst and ((len(stack) > 2 and cmd != get_previous_location().id) or len(stack) < 2):
                print("To miejsce jest za daleko!")
                possible_locations()
                continue

            import random as r
            missing_hp = game_mgr.player.base_hp - game_mgr.player.curr_hp

            curr_loc = szukanie(cmd)
            print("======", curr_loc.name, "======")
            print(curr_loc.entry_msg)
            game_mgr.player.regenerate_hp(r.randint(0, missing_hp // 2))
            move(game_mgr.player, cmd)
        else:
            print("Command not found. Use 'help' to show help.")
