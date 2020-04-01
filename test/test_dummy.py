import unittest

from mageknight.dummy import DummyPlayer
from mageknight.enums import Mana, DeedColor

class DummyPlayerTests(unittest.TestCase):
    def setUp(self):
        self.dummy = DummyPlayer()

    def test_add_cyrstal(self):
        self.dummy.add_crystal(Mana.GREEN)
        self.assertEqual(self.dummy.get_crytals()[Mana.GREEN],1)

    def test_add_invalid_crystal(self):
        with self.assertRaises(ValueError):
            self.dummy.add_crystal(Mana.GOLD)

    def test_process_turn_empty_deck(self):
        self.assertTrue(self.dummy.process_turn())

    def test_process_turn_one_card(self):
        self.assertTrue(self.dummy.process_turn())
        self.dummy.add_deed(DeedColor.GREEN)
        self.assertFalse(self.dummy.process_turn())
        self.assertTrue(self.dummy.process_turn())

    def test_process_turn_one_card_one_matching_crystal(self):
        self.assertTrue(self.dummy.process_turn())
        self.dummy.add_deed(DeedColor.GREEN)
        self.dummy.add_deed(DeedColor.GREEN)
        self.dummy.add_deed(DeedColor.GREEN)
        self.dummy.add_deed(DeedColor.GREEN)
        self.dummy.add_crystal(Mana.GREEN)
        self.assertFalse(self.dummy.process_turn())
        self.assertTrue(self.dummy.process_turn())

    def test_process_turn_one_card_one_other_crystal(self):
        self.assertTrue(self.dummy.process_turn())
        self.dummy.add_deed(DeedColor.GREEN)
        self.dummy.add_deed(DeedColor.GREEN)
        self.dummy.add_deed(DeedColor.GREEN)
        self.dummy.add_deed(DeedColor.GREEN)
        self.dummy.add_crystal(Mana.BLUE)
        self.assertFalse(self.dummy.process_turn())
        self.assertFalse(self.dummy.process_turn())
        self.assertTrue(self.dummy.process_turn())

if __name__ == "__main__":
    unittest.main()