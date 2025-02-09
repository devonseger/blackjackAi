from blackjack import deck
from blackjack import player
from blackjack import dealer


class Game:
    def __init__(self):
        self.deck = deck.Deck()
        print(len(self.deck.cards))
        self.player = player.Player()
        self.dealer = dealer.Dealer()
        
        self.start_game()


    def start_game(self):
        print("Welcome to BlackJack!")
        start = input("Enter 'start' to start a game!: ")
        if start.lower() != "start":
            return print("Exiting...")
        if len(self.deck.cards) == 52:
            for _ in range(2):
                self.dealer.hit(self.deck.deal_card())
                self.player.hit(self.deck.deal_card())
            self.dealer.reveal_first()
            self.player.reveal_cards()
        
