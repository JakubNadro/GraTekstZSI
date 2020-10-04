from gra.game import GameManager
from gra.ui import main_loop

game_mgr: GameManager

if __name__ == '__main__':
    print("Starting game...")
    # Initial steps
    game_mgr = GameManager()

    from gra.locationsystem import possible_locations, get_curr_location
    # Welcome message
    print("Witaj kozackiej grze fantasy! Aby zobaczyć dostępne polecenia wppisz 'help'. Poruszaj się między lokacjami\n"
          "Uzywając liczb odpowiadających numerowi lokalizacji, które będą wyświetlone poniżej. Walcz z potworami\n"
          "i zdobywaj doświadczenie.\n\n")
    # First level info
    print(get_curr_location().entry_msg)
    possible_locations()
    # Main game loop
    main_loop(game_mgr)
    # Exit prompt
    input("Aby wyjść wprowadź dowolny znak z klawiatury\n")
