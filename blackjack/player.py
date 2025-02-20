"""
This module defines the Player class, which represents a player in a game of Blackjack.

The Player class manages the player's hand, interacts with the bank for betting and payouts, 
and allows the player to draw (hit) and reveal cards.
"""

from blackjack import hand

class Player:
    """
    Represents a player in a Blackjack game.

    The Player class manages the player's hand, interacts with the bank for chip transactions, 
    and allows the player to draw cards.

    Attributes:
        hand (Hand): The player's current hand.
        bank (Bank): The player's bank for managing bets and payouts.
    """

    def __init__(self, name, bank):
        """
        Initializes a player with an empty hand and a bank for managing funds.
        """
        self.hand = hand.Hand()
        self.bank = bank  # This should be an instance, not a module reference.
        self.name = name

    def score(self):
        """Calculates and returns the player's current score based on their hand."""
        return self.hand.get_total()

    def hit(self, card):
        """
        Adds a card to the player's hand.

        Args:
            card (Card): The card to be added.

        Returns:
            str: A formatted string representing the card drawn.
        """
        self.hand.add_card(card)
        return "".join(f"{card.rank}{card.suit}")

    def reveal_cards(self):
        """
        Reveals all cards in the player's hand.
        """
        print(self.hand.cards)

    def __repr__(self):
        """Returns the player's name for easier debugging and display."""
        return self.name
