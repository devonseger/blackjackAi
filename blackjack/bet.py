class Bet:
    def __init__(self, bet, ratio=1.0):
        """Initialize a bet with bet amount and payout ratio."""
        self.bet = bet
        self.ratio = ratio
        self.result = None  # Win, Lose, Push
    
    def calculate_payout(self):
        """Handles calculating the payout if a player wins."""
        self.bet * self.ratio + self.bet
    
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
        return f"Bet(amount={self.amount}, payout_ratio={self.payout_ratio}, result={self.result})"