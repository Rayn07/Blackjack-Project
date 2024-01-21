from Animation import animation
from Hit_Stand import hit
import Cards as C
import Variables as v

def user_hit():
    user = int(v.user_hand.get())
    dealer = int(v.dealer_hand.get())
    if user > 10:
        C.CARD_VALUE_USER.update({"ace": 1})
    picked_card = hit(user, C.CARD_VALUE_USER)
    v.user_hand.set(value=picked_card[0])
    if v.card_num < 6:
        v.card_lst[v.card_num].set(value=picked_card[1])
        animation(v.user_card[v.card_num].place_info()["relx"], v.user_card[v.card_num].place_info()["rely"], v.user_card[v.card_num], v.card_num, v.card_lst)
    user = int(v.user_hand.get())
    v.card_num += 1