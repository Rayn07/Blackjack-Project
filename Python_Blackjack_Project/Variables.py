import customtkinter as c

token = c.StringVar(value=5)
user_hand = c.StringVar(value=0)
dealer_hand = c.StringVar(value=0)
dealer_hand_show = c.StringVar(value="?")
round_result = c.StringVar()
card_lst=["", c.StringVar(), c.StringVar(), c.StringVar(), c.StringVar(), c.StringVar(), c.StringVar(), c.StringVar()]
user_card = [None, None, None, None, None, None]
bot_card_lst=["", c.StringVar(), c.StringVar(), c.StringVar(), c.StringVar(), c.StringVar(), c.StringVar(), c.StringVar()]
bot_card = [None, None, None, None, None, None]
card_num = 1
bot_card_num = 1
n = 0