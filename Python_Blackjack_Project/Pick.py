import Cards as C
import random

def pick(card_value):
    suit, name = random.choice(list(C.CARDS_COPY.items()))
    name = random.choice(list(name.keys()))
    card = C.CARDS_COPY[suit].pop(name)
    C.CARD_COUNT.update({name: C.CARD_COUNT[name] - 1})
    if C.CARD_COUNT[name] == 0:
        C.CARD_NAME_COPY.remove(name)
    return card_value[name], card