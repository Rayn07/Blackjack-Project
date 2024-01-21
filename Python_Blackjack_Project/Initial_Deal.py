from Animation import *
from Pick import *
import Cards as C
import Variables as v

def initial_card_deal(n):
    for i in range(2):
        cards = pick(C.CARD_VALUE_USER), pick(C.CARD_VALUE_USER)
        init_dealt = cards[0][0] + cards[1][0]
        if init_dealt == 22:
            init_dealt = 12
        if i == 0:
            for j in range(2):
                v.bot_card_lst[v.bot_card_num].set(value=cards[j][1])
                v.bot_card_num += 1
        if i == 1:
            for j in range(2):
                v.card_lst[v.card_num].set(value=cards[j][1])
                animation(v.user_card[v.card_num].place_info()["relx"], v.user_card[v.card_num].place_info()["rely"], v.user_card[v.card_num], v.card_num, v.card_lst)
                v.card_num += 1
        C.INIT_DEALT_VALUES.append(init_dealt)
    v.dealer_hand.set(value=C.INIT_DEALT_VALUES[n + 0])
    v.user_hand.set(value=C.INIT_DEALT_VALUES[n + 1])