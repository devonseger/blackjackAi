from blackjack import hand

class Dealer:
    def __init__(self):
        self.hand = hand.Hand()
    
    def hit(self, card):
        self.hand.add_card(card)
        return "".join(f"{card.rank}{card.suit}")
    
    def reveal_first(self):
        print(f"Dealer's first card: {self.hand.cards[0].rank}{self.hand.cards[0].suit}")
        
    def reveal_cards(self):
        print(self.hand)
        
    def __repr__(self):
        return ", ".join(f"{card.rank}{card.suit}" for card in self.hand.cards)