from gra.game import GameManager
from gra.locationsystem import move


def quit_game(game_mgr: GameManager):
    global running
    running = False
    print("Zamykanie gry...")


def game_help(game_mgr: GameManager):
    print("Gracz:", game_mgr.player)
    print(cmds)


cmds = {
    "quit": quit_game,
    "help": game_help,
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
