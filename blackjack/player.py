from blackjack import hand
from blackjack import bank

class Player:
    def __init__(self):
        self.hand = hand.Hand()
        self.bank = bank
    
    def hit(self, card):
        self.hand.add_card(card)
        return "".join(f"{card.rank}{card.suit}")

    def reveal_cards(self):
        print(self.hand.cards)
        
    def __repr__(self):
        return ", ".join(f"{card.rank}{card.suit}" for card in self.hand.cards)
        