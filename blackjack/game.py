"""
This module defines the Game class, which controls the flow of a Blackjack game.

The Game class initializes the deck, player, dealer, and bank. It manages game rounds, 
checks for Blackjack and bust conditions, handles user input for hitting or standing, 
and determines the winner based on final hand values.
"""

from blackjack import deck
from blackjack import dealer
from blackjack.table import Table

class Game:
    """
    Controls the main flow of a Blackjack game.

    The Game class sets up the game by initializing the deck, player, dealer, and bank.
    It handles the turn-based logic of dealing cards, allowing player actions, 
    and determining the winner.

    Attributes:
        deck (Deck): The deck of cards used for the game.
        player (Player): The player participating in the game.
        dealer (Dealer): The dealer managing the house hand.
    """

    def __init__(self):
        """
        Initializes a new game instance.

        This method creates a deck of cards, initializes the player with a bank account,
        and sets up the dealer. It then starts the game loop.
        """
        self.deck = deck.Deck()
        print(f"Initialized Deck with: {len(self.deck.cards)} cards.")
        self.dealer = dealer.Dealer()
        self.table = Table()  # this should handle initalizing players
        self.start_game()

    def check_scores(self):
        """Compares each player's hand against the dealer and prints results."""
        dealer_score = self.dealer.hand.get_total()

        results = {}
        for player in self.table.players:
            player_score = player.hand.get_total()

            if player_score > 21:
                result = "Bust"
            elif player_score > dealer_score or dealer_score > 21:
                result = "Win"
            elif player_score < dealer_score:
                result = "Lose"
            else:
                result = "Push"

            results[player] = result
            print(f"{player} ({player_score}) vs Dealer ({dealer_score}): {result}")

        return results


    def is_bust(self, hand):
        """
        Checks if the given hand has gone over 21.

        Args:
            hand (Hand): The hand to check.

        Returns:
            bool: True if the hand value exceeds 21, otherwise False.
        """
        return hand.get_total() > 21

    def is_blackjack(self, hand):
        """
        Checks if the given hand is a Blackjack (21 with only two cards).

        Args:
            hand (Hand): The hand to check.

        Returns:
            bool: True if the hand value is exactly 21 with two cards, otherwise False.
        """
        return hand.get_total() == 21

    def check_initial_blackjacks(self):
        """Checks for Blackjacks immediately after the initial deal."""
        dealer_blackjack = self.is_blackjack(self.dealer.hand)

        # Track players who have blackjack
        players_with_blackjack = [player for player in self.table.players if self.is_blackjack(player.hand)]

        if dealer_blackjack and players_with_blackjack:
            print("Dealer and players have Blackjacks! Push!")
            return True  # Round ends (push)

        if dealer_blackjack:
            print("Dealer has Blackjack!")
            for player in self.table.players:
                if player not in players_with_blackjack:
                    print(f"{player.name} loses.")  # Now correctly prints player name
                else:
                    print(f"{player.name} pushes with the dealer.")
            return True  # Round ends immediately

        if players_with_blackjack:
            for player in players_with_blackjack:
                print(f"{player.name}'s cards: {player.hand}")
                print(f"{player.name} has Blackjack!!")
            return True  # Round ends for Blackjack players only

        return False  # No immediate Blackjacks, continue round


    def reveal_cards(self, hand):
        """
        Reveals all cards in the given hand.

        Args:
            hand (Hand): The hand to reveal.

        Returns:
            Hand: The hand object containing the revealed cards.
        """
        return hand

    def deal_cards(self):
        """
        Deals initial cards
        """
        if len(self.deck.cards) == 52:
            for _ in range(2):  # this will need to be updated to deal to all players/multiplayer
                for player in self.table.players:
                    player.hit(self.deck.deal_card())
                self.dealer.hit(self.deck.deal_card())
            self.dealer.reveal_first()  # Reveal only the dealer's first card

    def player_turn(self):  # handle player turns with this ex: for range _ in player(num_players)
        """
        Will be used to handle multiple players turns
        """
        for player in self.table.players:
            while True:
                action = input(f"Your cards: {player.hand} total: "
                            f"{player.hand.get_total()}, would you like to 'hit' or 'stand'?: ")
                if action == "hit":
                    nc = player.hit(self.deck.deal_card())
                    print(f"Added: {nc}")
                    if self.is_bust(player.hand):
                        print("Bust! You lose.")
                        return
                elif action == "stand":
                    break  # No additional logic is needed for stand
                else:
                    print("Please enter a valid choice.")

    def check_winners(self):
        """Checks final outcomes against the dealer and announces results."""
        dealer_score = self.dealer.hand.get_total()

        for player in self.table.players:
            player_score = player.hand.get_total()

            if self.is_bust(player.hand):
                print(f"{player} busts and loses.")
            elif self.is_bust(self.dealer.hand):
                print(f"{player} wins! Dealer bust.")
            elif player_score > dealer_score:
                print(f"{player} wins with {player_score}!")
            elif player_score < dealer_score:
                print(f"{player} loses with {player_score}. Dealer has {dealer_score}.")
            else:
                print(f"{player} pushes with the dealer at {player_score}.")


    def dealer_turn(self):
        """Dealer hits until they reach 17, but stays on a soft 17 if needed."""
        while self.dealer.hand.get_total() < 17:
            self.dealer.hit(self.deck.deal_card())
        # Check for soft 17 (Ace counted as 11)
        if self.dealer.hand.get_total() == 17 and any(card.rank == 'A'\
            '' for card in self.dealer.hand.cards):
            self.dealer.hit(self.deck.deal_card())  # Hit on soft 17


    def start_game(self):
        """
        Starts a new round of Blackjack.

        The dealer and player are each dealt two cards. The game then follows standard 
        Blackjack rules, allowing the player to hit or stand. The dealer reveals their 
        cards and draws until they reach at least 17. The game concludes with a winner 
        being determined.
        """

        self.deal_cards()
        if self.check_initial_blackjacks():
            return
        self.player_turn()
        self.dealer_turn()
        self.check_winners()
