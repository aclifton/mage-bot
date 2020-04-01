from mageknight.enums import Mana
from mageknight.enums import DeedColor
import random

class DeckEmptyError(BaseException):
    pass

class DummyPlayer:
    def __init__(self):
        self._crystals = {
            Mana.RED : 0,
            Mana.GREEN : 0,
            Mana.BLUE : 0,
            Mana.WHITE : 0,
        }

        self._deed_deck = []
        self._deed_discard = []

    def add_crystal(self, mana_color: Mana):
        if mana_color in [Mana.BLACK, Mana.GOLD]:
            raise ValueError("Invalid mana color")
        else:
            self._crystals[mana_color] = self._crystals[mana_color]+1

    def add_deed(self, deed_color: DeedColor):
        self._deed_deck.append(deed_color)

    def get_crytals(self):
        return self._crystals.copy()

    def reshuffle_deed_deck(self):
        self._deed_deck.extend(self._deed_discard)
        random.shuffle(self._deed_deck)
        self._deed_discard.clear()

    def draw_card(self):
        if len(self._deed_deck) == 0:
            raise DeckEmptyError()
        deed = self._deed_deck.pop()
        self._deed_discard.append(deed)
        return deed

    def process_turn(self):
        '''Returns True if end of is annouced'''

        if len(self._deed_deck) == 0:
            return True
        else:
            cards_to_draw = 3 if len(self._deed_deck) > 3 else len(self._deed_deck)
            for x in range(cards_to_draw):
                deed = self.draw_card()
            if deed is DeedColor.RED:
                cards_to_draw = self._crystals[Mana.RED]
            elif deed is DeedColor.GREEN:
                cards_to_draw = self._crystals[Mana.GREEN]
            elif deed is DeedColor.BLUE:
                cards_to_draw = self._crystals[Mana.BLUE]
            elif deed is DeedColor.WHITE:
                cards_to_draw = self._crystals[Mana.WHITE]
            elif deed is DeedColor.RED_GREEN:
                cards_to_draw = self._crystals[Mana.RED] + self._crystals[Mana.GREEN]
            elif deed is DeedColor.RED_WHITE:
                cards_to_draw = self._crystals[Mana.RED] + self._crystals[Mana.WHITE]
            elif deed is DeedColor.BLUE_GREEN:
                cards_to_draw = self._crystals[Mana.BLUE] + self._crystals[Mana.GREEN]
            elif deed is DeedColor.BLUE_WHITE:
                cards_to_draw = self._crystals[Mana.BLUE] + self._crystals[Mana.WHITE]
            else:
                raise Exception("Invalid deed color")

            cards_to_draw = cards_to_draw if len(self._deed_deck) > cards_to_draw else len(self._deed_deck)
            for x in range(cards_to_draw):
                self.draw_card()

        return False
        
