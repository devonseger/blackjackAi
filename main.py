from blackjack.game import Game

if __name__ == "__main__":
    print("Welcome to BlackJack!")
    while True:
        start = input("Enter 'start' to begin a new game!: ").strip().lower()
        if start == "start":
            game = Game()
        else:
            print("Exiting...")
            break