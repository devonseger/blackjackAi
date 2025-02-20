"""
This module defines the Hand class, which represents a hand of cards in the game.
It handles adding cards to the hand, calculating the total value of the hand, and
providing a string representation of the hand.
"""

class Hand:
    """
    Represents a hand of cards in the game.

    Attributes:
        cards (list): A list of cards in the hand.

    Methods:
        add_card(card):
            Adds a card to the hand.
        
        get_total() -> int:
            Calculates and returns the total value of the hand.
        
        __repr__() -> str:
            Returns a string representation of the hand.
    """
    def __init__(self):
        """Initialize an empty hand."""
        self.cards = []

    def add_card(self, card):
        """Adds a card to the hand.
        
        Args:
            card: The card to be added to the hand.
        """
        self.cards.append(card)

    def get_total(self):
        """Calculates and returns the total value of the hand.
        
        Returns:
            int: The total value of the hand, adjusting for aces.
        """
        total = sum(card.value for card in self.cards)
        aces = sum(1 for card in self.cards if card.rank == 'A')

        while total > 21 and aces:
            total -= 10  # subtract 10 to bring ace from 11 to 1
            aces -= 1
        return total

    def __repr__(self):
        """Returns a string representation of the hand.
        
        Returns:
            str: A string representation of the hand.
        """
        return ", ".join(f"{card.rank}{card.suit}" for card in self.cards)
