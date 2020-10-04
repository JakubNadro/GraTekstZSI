from gra.game import GameManager
from gra.locationsystem import move


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
    print("--- Informacje o graczu ---\n")
    print("HP:", game_mgr.player.curr_hp, " / ", game_mgr.player.base_hp, "\n")
    print("Broń:", game_mgr.player.weapon, "\n")


cmds = {
    "quit": quit_game,
    "help": game_help,
    "info": game_info
}

cmds_desc = {
    "help": "Wyświetla okienko pomocy",
    "quit": "Zamyka grę",
    "info": "Wyświetla informacje o graczu",
}

running: bool = True


def main_loop(game_mgr):
    while running:
        cmd = input(":")

        if cmd in cmds:
            cmds[cmd](game_mgr)
        elif cmd.isnumeric():
            move(game_mgr, int(cmd))
            print("Move to", cmd)
        else:
            print("Command not found. Use 'help' to show help.")
