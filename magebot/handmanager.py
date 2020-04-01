import random

class HandManagerError(BaseException):
    def __init__(self, text):
        super().__init__(text)

class NotInDeckError(HandManagerError):
    def __init__(self, text):
        super().__init__(text)

class NotInHandError(HandManagerError):
    def __init__(self, text):
        super().__init__(text)

class NotValidCardError(HandManagerError):
    def __init__(self, text):
        super().__init__(text)

class HandManager:
    def __init__(self):
        self._cards = list()
        self._deck = list()
        self._discard = list()
        self._hand = list()

    def register_card(self, card):
        self._cards.append(card)

    def throw_away_from_hand(self, card):
        if card not in self._hand:
            raise NotInHandError("")
        else:
            self._cards.remove(card)
            self._hand.remove(card)

    def add_to_top_deck(self, card):
        if card not in self._cards:
            raise NotValidCardError("Not in card list.")
        self._deck.append(card)
    
    def add_to_bottom_deck(self, card):
        if card not in self._cards:
            raise NotValidCardError("Not in card list.")
        self._deck.insert(0, card)

    def shuffle_deck(self):
        random.shuffle(self._deck)

    def draw(self):
        card = self._deck.pop()
        self._hand.append(card)
        return card

    def draw_specified(self, card):
        if card in self._deck:
            return card
        else:
            raise NotInDeckError("Not in deck")

    def discard_card(self, card):
        if card in self._hand:
            self._hand.remove(card)
            self._discard.append(card)
        else:
            raise NotInHandError("Not in hand")

    def add_discard_to_deck(self):
        self._deck.extend(self._discard)
        self._discard = list()
