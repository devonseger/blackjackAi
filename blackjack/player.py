from blackjack import hand

class Player:
    def __init__(self):
        self.hand = hand.Hand()
    
    def hit(self, card):
        self.hand.add_card(card)
    
    def Stand():
        # essentially just end turn, pass to dealer
        pass
    
    def Check_bust():
        # if sum cards > 21 then game over
        pass
    
    def reveal_cards(self):
        print(self.hand.cards)