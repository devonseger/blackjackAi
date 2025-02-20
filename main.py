"""
This module serves as the entry point for the Blackjack game.

It initializes and starts the game loop, allowing the player to begin a new round
or exit the game.
"""

from blackjack.game import Game

if __name__ == "__main__":
    print("Welcome to BlackJack!")

    while True:
        start = input("Enter 'start' to begin a new game!: ").strip().lower()

        if start == "start":
            game = Game()  # Initialize the game
        else:
            print("Exiting...")
            break
