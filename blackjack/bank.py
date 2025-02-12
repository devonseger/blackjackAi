from blackjack import bet

class Bank:
    def __init__(self):
        self.points = 1000   
    
    def bet(self, bet):
        """Handles betting for each player."""
        pass
    
    def payout(self):
        """Handles payouts for each player."""
        pass
    
    def get_balance(self):
        """Returns the players current balance."""
        pass
    
    def check_funds(self):
        """Check the players balance, used for denying entry to table if player has no chips."""
        
        pass