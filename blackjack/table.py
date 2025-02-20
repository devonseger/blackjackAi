"""This will handle table instance"""

from blackjack.bank import Bank
from blackjack.player import Player

class Table:
    """Manges multiple players at the table and their actions."""

    def __init__(self, num_players=1):  #default to 1 player unless specified.
        self.players = [Player(f"Player {i+1}", Bank()) for i in range(num_players)]
            # initialize players here, will need to figure out how to pass bank amount.

    def get_scores(self):
        """
        gathers scores for all players and stores them in a dict
        """
        return {player: player.hand.get_total() for player in self.players}

    def get_active_players(self):
        """
        Get number of active players at table.
        
        Returns:
            int: number of active players
        """
        return [player for player in self.players if player.bank.get_balance() > 0]  
            # Use balance to determine status

    def check_if_all_bust(self):
        """
        Check if all players are bust, if so skip dealer's turn as game is over
        
        Returns:
            true/false
        """
        return all(player.hand.get_total() > 21 for player in self.players)
    
    