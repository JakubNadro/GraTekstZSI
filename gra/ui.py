from gra.game import GameManager
from gra.locationsystem import move, get_curr_location


def quit_game(game_mgr: GameManager):
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
    print("HP:", game_mgr.player.curr_hp, " / ", game_mgr.player.base_hp)
    print("Punkty:", game_mgr.player.points)
    print("Broń:", game_mgr.player.weapon)
    print("---------------------------")


def game_pwd(game_mgr):
    print("Jesteś teraz w", get_curr_location().name)


cmds = {
    "quit": quit_game,
    "help": game_help,
    "info": game_info,
    "pwd": game_pwd()
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
        cmd = input(":")

        if cmd in cmds:
            cmds[cmd](game_mgr)
        elif cmd.isnumeric():
            cmd = int(cmd)

            if cmd not in get_curr_location().id_dst:
                print("To miejsce jest za daleko!")
                # TODO: print ten teges
                continue

            import random as r
            missing_hp = game_mgr.player.base_hp - game_mgr.player.curr_hp
            game_mgr.player.regenerate_hp(r.randint(0, missing_hp // 2))
            move(game_mgr, cmd)
            # print("Move to", cmd)
        else:
            print("Command not found. Use 'help' to show help.")
