# Card class - suit rank value

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = self.get_value()
        
    def get_value(self):
        if self.rank in ["J", "Q", "K"]:
            return 10
        if self.rank == "A":
            return 11 # Ace's value will start at 11, will implement logic for 11 or 1 later.
        else:
            return int(self.rank)
        
        
    def __repr__(self):
        return f"Card('{self.suit}', '{self.rank}')"
    