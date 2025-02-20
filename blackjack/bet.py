"""
This module defines the Bet class, which manages the betting logic in the game.
It handles bet initialization, calculating payouts, and determining the result of a bet.
"""

class Bet:
    """
    Represents a bet in the game with a specified amount and payout ratio.

    Attributes:
        bet (int): The amount of the bet.
        ratio (float): The payout ratio for the bet.
        result (str): The result of the bet, which can be 'win', 'lose', or 'push'.

    Methods:
        calculate_payout() -> int:
            Calculates the payout if the bet is won.
        
        lose() -> int:
            Handles a loss and returns 0.
        
        win() -> int:
            Handles a win and returns the calculated payout.
        
        push() -> int:
            Handles a draw and returns the bet amount.
        
        __repr__() -> str:
            Returns a string representation of the Bet instance.
    """
    def __init__(self, bet, ratio=1.0):
        """Initialize a bet with bet amount and payout ratio."""
        self.bet = bet
        self.ratio = ratio
        self.result = None  # Win, Lose, Push

    def calculate_payout(self):
        """Handles calculating the payout if a player wins."""
        return self.bet * self.ratio + self.bet

    def lose(self):
        """Handles a loss, returns 0."""
        self.result = "lose"
        return 0

    def win(self):
        """Handles a win, returns the payout using the calculate method."""
        self.result = "win"
        return self.calculate_payout()

    def push(self):
        """Handles a draw, return bet amount"""
        return self.bet

    def __repr__(self):
        return f"Bet(amount={self.bet}, payout_ratio={self.ratio}, result={self.result})"
