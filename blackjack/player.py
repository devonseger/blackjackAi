from blackjack import hand

class Player:
    def __init__(self):
        self.hand = hand.Hand()
        self.points = 1000
    
    def hit(self, card):
        self.hand.add_card(card)
        return "".join(f"{card.rank}{card.suit}")

    def reveal_cards(self):
        print(self.hand.cards)