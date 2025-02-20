"""
This module defines the Bank class, which manages player funds, 
handles bets, payouts, and checks for sufficient balance.
"""
class Bank:
    """
    Manages the player's balance, handling bets, payouts, and fund validation.

    The Bank class is responsible for tracking the player's available chips, 
    deducting bets, adding winnings, and ensuring players have enough funds 
    to continue playing. 

    Attributes:
        points (int): The player's current balance in chips.

    Methods:
        bet(amount: int) -> bool:
            Deducts the bet amount if sufficient funds are available.
            Returns True if the bet is placed, otherwise False.

        payout(payout: int) -> None:
            Adds the specified amount to the player's balance after a win.

        get_balance() -> int:
            Returns the player's current balance.

        check_funds(amount: int) -> bool:
            Checks if the player has enough chips for a given action.
            Returns True if funds are sufficient, otherwise False.
    """
    def __init__(self, initial_balance=1000):  # accept init bal, or default 1k
        self.points = initial_balance

    def bet(self, amount):
        """Handles betting for each player."""
        if amount > self.points:
            print("Not enough chips! You cannot place this bet.")
            return False

        self.points -= amount
        print(f"Bet of {amount} placed. You have {self.points} remaining.")
        return True

    def payout(self, payout):
        """Handles payouts for each player."""
        self.points += payout

    def get_balance(self):
        """Returns the players current balance."""
        return self.points


    def check_funds(self, amount):
        """Returns True if the player has enough funds, False otherwise."""
        if self.points < amount:
            print(f"Not enough chips! You currently have {self.points} chips.")
            return False
        return True
