import random
from blackjack.card import Card  # ✅ Correct import path

class Deck:
    def __init__(self):
        """Initialize the deck with 52 cards."""
        suits = ['♠', '♣', '♦', '♥']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.cards = [Card(suit, rank) for suit in suits for rank in ranks]
        self.shuffle()
        
        
    def shuffle(self):
        """Shuffle the deck."""
        random.shuffle(self.cards)

    def deal_card(self):
        """Deal a card from the deck."""
        return self.cards.pop() if self.cards else None  # Returns None if deck is empty