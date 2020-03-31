import unittest

from magebot.handmanager import HandManager
from magebot.handmanager import NotInDeckError
from magebot.handmanager import NotInHandError
from magebot.handmanager import NotValidCardError

class HandManagerTests(unittest.TestCase):
    def setUp(self):
        self.manager = HandManager()

    def test_add_card(self):
        self.manager.register_card(1)
        self.manager.add_to_top_deck(1)

    def test_draw_card(self):
        self.manager.register_card(1)
        self.manager.add_to_top_deck(1)
        card = self.manager.draw()
        self.assertEqual(card, 1)

    def test_discard_card(self):
        self.manager.register_card(1)
        self.manager.add_to_top_deck(1)
        card = self.manager.draw()
        self.manager.discard_card(card)

    def test_discard_card_not_in_deck(self):
        self.manager.register_card(1)
        self.manager.add_to_top_deck(1)
        self.manager.draw()
        with self.assertRaises(NotInHandError):
            self.manager.discard_card(2)

    def test_discard_card_not_in_hand(self):
        self.manager.register_card(1)
        self.manager.add_to_top_deck(1)
        self.manager.draw()
        with self.assertRaises(NotInHandError):
            self.manager.discard_card(2)

    def test_draw_from_top(self):
        self.manager.register_card(1)
        self.manager.register_card(2)
        self.manager.add_to_top_deck(1)
        self.manager.add_to_top_deck(2)
        self.assertEqual(self.manager.draw(), 2)
        self.assertEqual(self.manager.draw(), 1)

    def test_draw_from_top_2(self):
        self.manager.register_card(1)
        self.manager.register_card(2)
        self.manager.add_to_bottom_deck(1)
        self.manager.add_to_bottom_deck(2)
        self.assertEqual(self.manager.draw(), 1)
        self.assertEqual(self.manager.draw(), 2)
        

if __name__ == "__main__":
    unittest.main()