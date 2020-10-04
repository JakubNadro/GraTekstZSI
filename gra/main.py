from gra.game import GameManager
from gra.ui import main_loop

game_mgr: GameManager

if __name__ == '__main__':
    print("Starting game...")
    game_mgr = GameManager()
    main_loop(game_mgr)
    input("Aby wyjść wciśnij dowolny znak na klawiaturze\n")
