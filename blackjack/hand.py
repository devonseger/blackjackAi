class Hand:
    def __init__(self):
        self.cards = []
        

    def add_card(self, card):
        self.cards.append(card)
        
    def get_total(self):
        total = sum(card.value for card in self.cards)
        aces = sum(1 for card in self.cards if card.rank == 'A')
        
        while total > 21 and aces:
            total -= 10 # subtract 10 to bring ace from 11 to 1
            aces -= 1
        return total
        
    def __repr__(self):
        self.cards
        return ", ".join(f"{card.rank}{card.suit}" for card in self.cards)
        