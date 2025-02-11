import unittest
import logging
from blackjack.card import Card
from blackjack.deck import Deck
from blackjack.hand import Hand
from blackjack.player import Player
from blackjack.dealer import Dealer

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class TestCard(unittest.TestCase):
    def test_card_value(self):
        card = Card('♠', 'A')
        self.assertEqual(card.value, 11)
        logger.info(f'TestCard: {card} value is {card.value}')
        card = Card('♠', 'K')
        self.assertEqual(card.value, 10)
        logger.info(f'TestCard: {card} value is {card.value}')
        card = Card('♠', '5')
        self.assertEqual(card.value, 5)
        logger.info(f'TestCard: {card} value is {card.value}')

class TestDeck(unittest.TestCase):
    def test_deck_initialization(self):
        deck = Deck()
        self.assertEqual(len(deck.cards), 52)
        logger.info(f'TestDeck: Deck initialized with {len(deck.cards)} cards')

    def test_deck_shuffle(self):
        deck = Deck()
        cards_before_shuffle = deck.cards.copy()
        deck.shuffle()
        self.assertNotEqual(deck.cards, cards_before_shuffle)
        logger.info('TestDeck: Deck shuffled')

    def test_deal_card(self):
        deck = Deck()
        card = deck.deal_card()
        self.assertIsInstance(card, Card)
        self.assertEqual(len(deck.cards), 51)
        logger.info(f'TestDeck: Dealt {card}, {len(deck.cards)} cards remaining')

class TestHand(unittest.TestCase):
    def test_hand_add_card(self):
        hand = Hand()
        card = Card('♠', 'A')
        hand.add_card(card)
        self.assertEqual(len(hand.cards), 1)
        self.assertEqual(hand.cards[0], card)
        logger.info(f'TestHand: Added {card} to hand')

    def test_hand_total(self):
        hand = Hand()
        hand.add_card(Card('♠', 'A'))
        hand.add_card(Card('♠', 'K'))
        self.assertEqual(hand.get_total(), 21)
        logger.info(f'TestHand: Hand total is {hand.get_total()}')
        hand.add_card(Card('♠', '5'))
        self.assertEqual(hand.get_total(), 16)
        logger.info(f'TestHand: Hand total is {hand.get_total()}')

class TestPlayer(unittest.TestCase):
    def test_player_initialization(self):
        player = Player()
        self.assertEqual(player.points, 1000)
        self.assertEqual(len(player.hand.cards), 0)
        logger.info(f'TestPlayer: Player initialized with {player.points} points and {len(player.hand.cards)} cards in hand')

    def test_player_hit(self):
        player = Player()
        card = Card('♠', 'A')
        player.hit(card)
        self.assertEqual(len(player.hand.cards), 1)
        self.assertEqual(player.hand.cards[0], card)
        logger.info(f'TestPlayer: Player hit with {card}')

class TestDealer(unittest.TestCase):
    def test_dealer_initialization(self):
        dealer = Dealer()
        self.assertEqual(len(dealer.hand.cards), 0)
        logger.info('TestDealer: Dealer initialized with empty hand')

    def test_dealer_hit(self):
        dealer = Dealer()
        card = Card('♠', 'A')
        dealer.hit(card)
        self.assertEqual(len(dealer.hand.cards), 1)
        self.assertEqual(dealer.hand.cards[0], card)
        logger.info(f'TestDealer: Dealer hit with {card}')

if __name__ == '__main__':
    unittest.main()