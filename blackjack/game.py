from blackjack import deck
from blackjack import player
from blackjack import dealer


class Game:
    def __init__(self):
        self.deck = deck.Deck()
        print(f"Initialized Deck with: {len(self.deck.cards)} cards.")
        self.player = player.Player()
        self.dealer = dealer.Dealer()
        
        self.start_game()
        
    def check_scores(self):
        dealer_score = self.dealer.hand.get_total()
        player_score = self.player.hand.get_total()

        if player_score > dealer_score:
            return 1  # Player wins
        elif dealer_score > player_score:
            return 0  # Dealer wins
        else:
            return 2  # It's a tie (Push)

        
    def is_bust(self, hand):
        """Returns True if hand value is over 21."""
        return hand.get_total() > 21
    
    def is_blackjack(self, hand):
        """returns True if blackjack"""
        return hand.get_total() == 21
    
    def reveal_cards(self, hand):
        return hand

    def start_game(self):
        if len(self.deck.cards) == 52:
            for _ in range(2):
                self.dealer.hit(self.deck.deal_card())
                self.player.hit(self.deck.deal_card())
            self.dealer.reveal_first() # If ace offer insurance? then check if blackjack
            print(f"Revealing player cards: {self.reveal_cards(self.player)}")
            if self.dealer.hand.cards[0].rank == "A":
                print("First card is an ace")
                # Insurance?
                if self.is_blackjack(self.dealer.hand):
                    print("Dealer Blackjack!\nGame Over!")
                    return
                
        if self.is_blackjack(self.player.hand):
            print("Blackjack!\nYou win!") # blackjack is displayed properly but player never sees their cards.
            return
        
        while True:
            action = input(f"Your cards: {self.player.hand} total: {self.player.hand.get_total()}, would you like to 'hit' or 'stand'?: ")
            if action == "hit":
                nc = self.player.hit(self.deck.deal_card())
                print(f"Added: {nc}")
                if self.is_bust(self.player.hand):
                    print("Bust! You lose.")
                    return
            elif action == "stand":
                break # probably don't actually need stand logic since its essentially just a break.
            else:
                print("Please enter a valid choice.")
        print(f"Dealer has: {self.dealer.hand} total: {self.dealer.hand.get_total()}")
        while True:
            if self.dealer.hand.get_total() <= 16:
                print("Dealer hits.")
                dnc = self.dealer.hit(self.deck.deal_card())
                print(f"Added: {dnc}")
            if self.is_bust(self.dealer.hand):
                print("Dealer Bust! You win!!")
                return
            if self.dealer.hand.get_total() > 16:
                break
        
        print(f"player : {self.player.hand.get_total()} dealer : {self.dealer.hand.get_total()}")
        # Compare values and determine winner
        if self.check_scores() == 1:
            print("You win!")
        elif self.check_scores() == 0:
            print("You lose!")
        else:
            print("Push!")
    