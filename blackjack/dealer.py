"""
This module defines the Dealer class, which represents the dealer in a game of Blackjack.

The Dealer class manages the dealer's hand, handles drawing cards (hitting), 
and reveals cards as per Blackjack rules.
"""

from blackjack import hand

class Dealer:
    """
    Represents the dealer in a Blackjack game.

    The Dealer manages their own hand, can draw cards, and reveal cards as per game rules.

    Attributes:
        hand (Hand): The dealer's current hand.
    """

    def __init__(self):
        """
        Initializes the dealer with an empty hand.
        """
        self.hand = hand.Hand()
        
    def score(self):
        """
        calculates and returns the dealer's current score
        """
        return self.hand.get_total()

    def hit(self, card):
        """
        Adds a card to the dealer's hand.

        Args:
            card (Card): The card to be added.

        Returns:
            str: A formatted string representing the card drawn.
        """
        self.hand.add_card(card)
        return "".join(f"{card.rank}{card.suit}")

    def reveal_first(self):
        """
        Reveals only the first card in the dealer's hand, as per Blackjack rules.

        This is used at the beginning of the game when the dealer's second card is hidden.
        """
        print(f"Dealer's first card: {self.hand.cards[0].rank}{self.hand.cards[0].suit}")

    def reveal_cards(self):
        """
        Reveals all cards in the dealer's hand.
        """
        print(self.hand)

    def __repr__(self):
        """
        Returns a string representation of the dealer's hand.

        Returns:
            str: A formatted string showing all cards in the dealer's hand.
        """
        return ", ".join(f"{card.rank}{card.suit}" for card in self.hand.cards)
