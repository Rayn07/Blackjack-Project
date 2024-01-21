from copy import deepcopy
import Cards as C

def card_refresh():
    for card in C.CARD_NAME:
        C.CARD_COUNT.update({card: 4})
    C.CARD_NAME_COPY = C.CARD_NAME.copy()
    C.CARDS_COPY = deepcopy(C.CARDS)
    C.CARD_VALUE_USER.update({"ace": 11})
    C.CARD_VALUE_DEALER.update({"ace": 11})