# Card class - suit rank value

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        
        
    def __repr__(self):
        return f"Card('{self.suit}', '{self.rank}')"