from Hit_Stand import hit
import Cards as C
import Variables as v
import random

def chance(diff):
    psf = 9 - diff  # psf = percent subtraction factor
    if random.randint(1, 100) <= (70 - (8 * psf)):  # Derived using Bernoulli's Theorem
        return True

def bot_logic():
    dealer = int(v.dealer_hand.get())
    diff = 21 - dealer
    while diff > 0:
        dealer = int(v.dealer_hand.get())
        diff = 21 - dealer
        if dealer > 10:
            C.CARD_VALUE_DEALER.update({"ace": 1})
        if diff >= 10:
            card = hit(dealer, C.CARD_VALUE_DEALER)
            v.dealer_hand.set(value=card[0])
            v.bot_card_lst[v.bot_card_num].set(value=card[1])
            v.bot_card_num += 1
        else:
            if chance(diff) == True:
                card = hit(dealer, C.CARD_VALUE_DEALER)
                v.dealer_hand.set(value=card[0])
                v.bot_card_lst[v.bot_card_num].set(value=card[1])
                v.bot_card_num += 1
            else:
                break