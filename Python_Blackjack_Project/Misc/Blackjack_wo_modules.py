# pip install customtkinter
# pip install Pillow
# pip install pygame
import customtkinter as c
from PIL import Image
import random
import pygame as p
from copy import deepcopy

# *****************************APP-ATTRIBUTES*********************************#
app = c.CTk(fg_color="#0681B1")
app.geometry("1200x850")
app.title("Blackjack Mini Project")
app.iconbitmap("Images/Blackjack.ico")
# app.attributes('-fullscreen', True)

p.mixer.init()
# ****************************************************************************#


# ****************************VARIABLES***************************************#
token = c.StringVar(value=5)
user_hand = c.StringVar(value=0)
dealer_hand = c.StringVar(value=0)
dealer_hand_show = c.StringVar(value="?")
round_result = c.StringVar()
card_lst=["", c.StringVar(), c.StringVar(), c.StringVar(), c.StringVar(), c.StringVar(), c.StringVar(), c.StringVar()]
bot_card_lst=["", c.StringVar(), c.StringVar(), c.StringVar(), c.StringVar(), c.StringVar(), c.StringVar(), c.StringVar()]
card_num = 1
bot_card_num = 1
movex, movey = 0, 0
n = 0

INIT_DEALT_VALUES = []
CARDS = {
    "spades": {
        "ace": "🂡","two": "🂢", "three": "🂣", "four": "🂤", "five": "🂥", "six": "🂦", "seven": "🂧",
        "eight": "🂨", "nine": "🂩", "ten": "🂪", 'jack': "🂫", "queen": "🂭", "king": "🂮"
    },

    "hearts": {
        "ace": "🂱","two": "🂲", "three": "🂳", "four": "🂴", "five": "🂵", "six": "🂶", "seven": "🂷",
        "eight": "🂸", "nine": "🂹", "ten": "🂺", 'jack': "🂻", "queen": "🂽", "king": "🂾"
    },

    "diamonds": {
        "ace": "🃁","two": "🃂", "three": "🃃", "four": "🃄", "five": "🃅", "six": "🃆", "seven": "🃇",
        "eight": "🃈", "nine": "🃉", "ten": "🃊", 'jack': "🃋", "queen": "🃍", "king": "🃎"
    },

    "clubs": {
        "ace": "🃑","two": "🃒", "three": "🃓", "four": "🃔", "five": "🃕", "six": "🃖", "seven": "🃗",
        "eight": "🃘", "nine": "🃙", "ten": "🃚", 'jack': "🃛", "queen": "🃝", "king": "🃞"
    }
}
CARD_NAME = [
    "ace", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
    "jack", "queen", "king"
]
CARD_SUITS = ["spades", "hearts", "diamonds", "clubs"]
CARD_COUNT = {
    "two": 4, "three": 4, "four": 4, "five": 4, "six": 4, "seven": 4, "eight": 4, "nine": 4, "ten": 4,
    "jack": 4, "king": 4, "queen": 4, "ace": 4
}
CARD_VALUE_USER = {
    "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10,
    "jack": 10, "king": 10, "queen": 10, "ace": 11
}
CARD_VALUE_DEALER = {
    "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10,
    "jack": 10, "king": 10, "queen": 10, "ace": 11
}
CARDS_COPY = deepcopy(CARDS)
CARD_NAME_COPY = CARD_NAME.copy()
# ****************************************************************************#


# ********************************IMAGES**************************************#
blank = c.CTkImage(light_image=Image.open("Images/Blank.png"))
logo = c.CTkImage(
    light_image=Image.open("Images/Blackjack_Logo.png"),
    size=(760, 220),
)
stack = c.CTkImage(
    light_image=Image.open("Images/Card_Stack.png"),
    size=(205, 170),
)
card_design = c.CTkImage(
    light_image=Image.open("Images/Card_Design.jpg"),
    size=(105, 160),
)
# ****************************************************************************#


# ******************************FUNCTIONS*************************************#
def animation(x, y, label, n, card_list):
    def move():
        global movex, movey
        label.configure(image=card_design)
        stackx, stacky = 0.875, 0.47
        incx = (eval(x) - stackx)/100.0
        incy = (eval(y) - stacky)/100.0
        movex += incx
        movex = round(movex, 4)
        movey += incy
        movey = round(movey, 4)
        label.place_configure(relx=stackx + movex,rely=stacky + movey, anchor='center')
        if stackx + movex > eval(x):
            label.after(1, move)
        else:
            movex, movey = 0, 0
            label.configure(textvariable=card_list[n], image=blank)
            label.place_configure(relx=eval(x),rely=eval(y), anchor='center')
    move()

def start():
    p.mixer_music.load("Sounds/Start_Button_Sound.mp3")
    p.mixer_music.play()
    gamespace("inplay")
    home.pack_forget()
    initial_card_deal(n)
    bot_logic()


# Pick random cards
def pick(card_value):
    suit, name = random.choice(list(CARDS_COPY.items()))
    name = random.choice(list(name.keys()))
    card = CARDS_COPY[suit].pop(name)
    CARD_COUNT.update({name: CARD_COUNT[name] - 1})
    if CARD_COUNT[name] == 0:
        CARD_NAME_COPY.remove(name)
    return card_value[name], card


# Card count returns back to 4
def card_refresh():
    global CARDS_COPY, CARD_NAME_COPY
    for card in CARD_NAME:
        CARD_COUNT.update({card: 4})
    CARD_NAME_COPY = CARD_NAME.copy()
    CARDS_COPY = deepcopy(CARDS)


# Initial Card Distribution
def initial_card_deal(n):
    global user_hand, dealer_hand, card_num, bot_card_num
    for i in range(2):
        cards = pick(CARD_VALUE_USER), pick(CARD_VALUE_USER)
        init_dealt = cards[0][0] + cards[1][0]
        if init_dealt == 22:
            init_dealt = 12
        if i == 0:
            for j in range(2):
                bot_card_lst[bot_card_num].set(value=cards[j][1])
                bot_card_num += 1
        if i == 1:
            for j in range(2):
                card_lst[card_num].set(value=cards[j][1])
                animation(user_card[card_num].place_info()["relx"], user_card[card_num].place_info()["rely"], user_card[card_num], card_num, card_lst)
                card_num += 1
        INIT_DEALT_VALUES.append(init_dealt)
    dealer_hand.set(value=INIT_DEALT_VALUES[n + 0])
    user_hand.set(value=INIT_DEALT_VALUES[n + 1])


# Logic for the bot to decide whether to hit or stand
def bot_logic():
    global dealer_hand, bot_card_num
    dealer = int(dealer_hand.get())
    diff = 21 - dealer
    while diff > 0:
        dealer = int(dealer_hand.get())
        diff = 21 - dealer
        if dealer > 10:
            CARD_VALUE_DEALER.update({"ace": 1})
        if diff >= 10:
            card = hit(dealer, CARD_VALUE_DEALER)
            dealer_hand.set(value=card[0])
            bot_card_lst[bot_card_num].set(value=card[1])
            bot_card_num += 1
        else:
            if chance(diff) == True:
                card = hit(dealer, CARD_VALUE_DEALER)
                dealer_hand.set(value=card[0])
                bot_card_lst[bot_card_num].set(value=card[1])
                bot_card_num += 1
            else:
                break


# Hit by user
def user_hit():
    p.mixer_music.load("Sounds/Card_Drawn_Sound.mp3")
    p.mixer_music.play()
    global card_num
    user = int(user_hand.get())
    dealer = int(dealer_hand.get())
    if user > 10:
        CARD_VALUE_USER.update({"ace": 1})
    picked_card = hit(user, CARD_VALUE_USER)
    user_hand.set(value=picked_card[0])
    if card_num < 6:
        card_lst[card_num].set(value=picked_card[1])
        animation(user_card[card_num].place_info()["relx"], user_card[card_num].place_info()["rely"], user_card[card_num], card_num, card_lst)
    user = int(user_hand.get())
    dealer = int(dealer_hand.get())
    card_num += 1
    if user > 21:
        stand(user, dealer)

# Probability of hit for bot
def chance(diff):
    psf = 9 - diff  # psf = percent subtraction factor
    if random.randint(1, 100) <= (70 - (8 * psf)):  # Bernoulli's Theorem n that B)
        return True


# Commands
def hit(hand, card_value):
    picked = pick(card_value)
    card = picked[1]
    hand = hand + picked[0]
    return hand, card


def stand(user, dealer):
    p.mixer_music.load("Sounds/Stand_Clicking_Sound.mp3")
    p.mixer_music.play()
    global token
    tok = int(token.get())
    print("Dealer's Final Hand:", dealer)
    print("Your Final Hand:", user)
    if user > 21 and dealer > 21:
        print("Round draw")
        round_result.set(value="Round Draw")
    elif user > 21 and dealer <= 21:
        print("Dealer wins this round")
        token.set(tok // 2)
        round_result.set(value="Round Lost")
    elif dealer > 21 and user <= 21:
        print("You win this round!")
        token.set(tok * 2)
        round_result.set(value="Round Won")
    elif user > dealer:
        print("You win this round!")
        token.set(tok * 2)
        round_result.set(value="Round Won")
    elif user == dealer:
        print("Round draw")
        round_result.set(value="Round Draw")
    else:
        print("Dealer wins this round")
        token.set(tok // 2)
        round_result.set(value="Round Lost")
    tok = int(token.get())
    if tok > 50:
        token.set(50)
    gamespace("end")


def round_end():
    p.mixer_music.load("Sounds/Card_Drawn_Sound.mp3")
    p.mixer_music.play()
    global dealer_hand, user_hand, card_num, bot_card_num, n
    if int(token.get()) == 50:
        app.configure(fg_color="#292F36")
        win_screen()
        game["end"].pack_forget()
        return
    elif int(token.get()) == 0:
        app.configure(fg_color="#292F36")
        lose_screen()
        game["end"].pack_forget()
        return
    card_num = 1
    bot_card_num = 1
    for i in range(1,6):
        bot_card_lst[i].set("")
        card_lst[i].set("")
    card_refresh()
    n += 2
    gamespace("inplay")
    game["end"].pack_forget()
    initial_card_deal(n)
    bot_logic()
# ****************************************************************************#


# *****************************HOMEPAGE***************************************#
font = c.CTkFont(family="Corbel", size=48, slant="italic", weight="bold")

wid = app.winfo_screenwidth()
heig = app.winfo_screenheight()

home = c.CTkFrame(app, fg_color="#0681B1", height=heig, width=wid)

logo_label = c.CTkLabel(
    home,
    image=logo,
    font=font,
    text_color="#FECD48",
    text="Closest to Twenty-One",
    compound="top",
)

start = c.CTkButton(
    home,
    corner_radius=24,
    font=c.CTkFont(family="Arial Rounded MT Bold", size=96, weight="bold"),
    text_color="#F5F0F6",
    text="START",
    fg_color="#045676",
    hover_color="#1A4C60",
    command=start,
)

home.pack()
logo_label.place(rely=0.18, relx=0.5, anchor="center")
start.place(rely=0.6, relx=0.5, anchor="center")
# ***************************************************************************#


# *****************************GAMESPACE*************************************#
game = {"inplay": None, "end": None}

user_card = [None, None, None, None, None, None]
bot_card = [None, None, None, None, None, None]

def gamespace(screen):
    global blank

    dealer_hand_show.set(value="?")

    wid = app.winfo_screenwidth()
    heig = app.winfo_screenheight()

    game[screen] = c.CTkFrame(app, fg_color="#0681B1", width=wid, height=heig)


    if screen == "end":
        dealer_hand_show.set(value=dealer_hand.get())
            
        next_round = c.CTkButton(
            game[screen],
            corner_radius=12,
            font=c.CTkFont(family="Bahnschrift SemiBold", size=48, weight="bold"),
            text_color="#344433",
            text="NEXT ROUND",
            fg_color="#FECD48",
            hover_color="#FEBD0B",
            command=round_end,
            height=64,
            border_width=4,
            border_color="#CB9501"
        )

        result = c.CTkLabel(
            game[screen],
            textvariable=round_result,
            font=c.CTkFont(family="Arial Rounded MT Bold", size=56, weight="bold"),
            text_color="#000000",
        )

        next_round.place(rely=0.5, relx=0.15, anchor="center")
        result.place(rely=0.5, relx=0.5, anchor="center")
        game["inplay"].pack_forget()


    card_stack = c.CTkButton(
        game[screen],
        image=stack,
        text="",
        command=user_hit,
        fg_color="transparent",
        hover="false"
    )

    stand_but = c.CTkButton(
        game[screen],
        corner_radius=12,
        font=c.CTkFont(family="Arial Rounded MT Bold", size=48, weight="bold"),
        text_color="#C5FE9A",
        text="STAND",
        fg_color="#045676",
        hover_color="#1A4C60",
        command=lambda: stand(int(user_hand.get()), int(dealer_hand.get())),
        height=64,
    )

    token_label = c.CTkLabel(
        game[screen],
        text="Tokens",
        font=c.CTkFont(family="Malgun Gothic", size=36, weight="bold"),
        text_color="#EBEBFF",
    )

    token_counter = c.CTkButton(
        game[screen],
        textvariable=token,
        font=c.CTkFont(family="Malgun Gothic", size=48, weight="bold"),
        text_color="#EBEBFF",
        fg_color="#7BB77B",
        corner_radius=24,
        width=120,
        anchor="n",
        hover="false",
        border_width=4,
        border_color="#335C33",
    )

    user_name = c.CTkLabel(
        game[screen],
        text="😃 YOU",
        font=c.CTkFont(family="Small Fonts", size=48, weight="bold"),
        text_color="#010010",
    )

    user_card[1] = c.CTkLabel(
        game[screen],
        text="",
        textvariable=card_lst[0],
        image=None,
        font=c.CTkFont(size=192),
        text_color="#000000",
        fg_color="transparent",
        bg_color="transparent"
    )

    user_card[2] = c.CTkLabel(
        game[screen],
        text="",
        textvariable=card_lst[0],
        image=None,
        font=c.CTkFont(size=192),
        text_color="#000000",
    )

    user_card[3] = c.CTkLabel(
        game[screen],
        text="",
        textvariable=card_lst[0],
        image=None,
        font=c.CTkFont(size=192),
        text_color="#000000",
    )

    user_card[4] = c.CTkLabel(
        game[screen],
        text="",
        textvariable=card_lst[0],
        image=None,
        font=c.CTkFont(size=192),
        text_color="#000000",
    )

    user_card[5] = c.CTkLabel(
        game[screen],
        text="",
        textvariable=card_lst[0],
        image=None,
        font=c.CTkFont(size=192),
        text_color="#000000",
    )

    user_score = c.CTkButton(
        game[screen],
        textvariable=user_hand,
        font=c.CTkFont(family="Malgun Gothic", size=48, weight="bold"),
        text_color="#EBEBFF",
        fg_color="#335F70",
        corner_radius=24,
        width=240,
        anchor="n",
        hover="false",
        border_width=4,
        border_color="#264653",
    )

    bot_card[1] = c.CTkLabel(
        game[screen],
        text="",
        textvariable=bot_card_lst[0],
        image=card_design,
        font=c.CTkFont(size=192),
        text_color="#000000",
    )

    bot_card[2] = c.CTkLabel(
        game[screen],
        text="",
        textvariable=bot_card_lst[0],
        image=card_design,
        font=c.CTkFont(size=192),
        text_color="#000000",
    )

    bot_card[3] = c.CTkLabel(
        game[screen],
        text="",
        textvariable=bot_card_lst[0],
        image=card_design,
        font=c.CTkFont(size=192),
        text_color="#000000",
    )

    bot_card[4] = c.CTkLabel(
        game[screen],
        text="",
        textvariable=bot_card_lst[0],
        image=card_design,
        font=c.CTkFont(size=192),
        text_color="#000000",
    )

    bot_card[5] = c.CTkLabel(
        game[screen],
        text="",
        textvariable=bot_card_lst[0],
        image=card_design,
        font=c.CTkFont(size=192),
        text_color="#000000",
    )

    bot_name = c.CTkLabel(
        game[screen],
        text="🤖 BOT",
        font=c.CTkFont(family="Small Fonts", size=48, weight="bold"),
        text_color="#FEFFFE",
    )

    bot_score = c.CTkButton(
        game[screen],
        textvariable=dealer_hand_show,
        font=c.CTkFont(family="Malgun Gothic", size=48, weight="bold"),
        text_color="#EBEBFF",
        fg_color="#D54D50",
        corner_radius=24,
        width=240,
        anchor="n",
        hover="false",
        border_width=4,
        border_color="#A5272B",
    )
    game[screen].pack()
    token_counter.place(rely=0.1, relx=0.1, anchor="center")
    token_label.place(rely=0.18, relx=0.1, anchor="center")
    stand_but.place(rely=0.78, relx=0.875, anchor="center")
    user_score.place(rely=0.62, relx=0.5, anchor="center")
    bot_score.place(rely=0.385, relx=0.5, anchor="center")
    card_stack.place(rely=0.47, relx=0.875, anchor="center")
    user_card[1].place(rely=0.795, relx=0.3, anchor="center")
    user_card[2].place(rely=0.795, relx=0.4, anchor="center")
    user_card[3].place(rely=0.795, relx=0.5, anchor="center")
    user_card[4].place(rely=0.795, relx=0.6, anchor="center")
    user_card[5].place(rely=0.795, relx=0.7, anchor="center")
    user_name.place(rely=0.95, relx=0.5, anchor="center")
    bot_card[1].place(rely=0.2, relx=0.3, anchor="center")
    bot_card[2].place(rely=0.2, relx=0.4, anchor="center")
    bot_card[3].place(rely=0.2, relx=0.5, anchor="center")
    bot_card[4].place(rely=0.2, relx=0.6, anchor="center")
    bot_card[5].place(rely=0.2, relx=0.7, anchor="center")
    bot_name.place(rely=0.05, relx=0.5, anchor="center")

    if screen == "end":
        stand_but.configure(state="disabled")
        card_stack.configure(state="disabled")
        if int(token.get()) == 50 or int(token.get()) == 0:
            next_round.configure(text="END GAME")
        for i in range(1,6):
            user_card[i].configure(textvariable=card_lst[i], image=blank)
            bot_card[i].configure(textvariable=bot_card_lst[i], image=blank)
# ***************************************************************************#


# *************************************WIN***********************************#
def win_screen():
    p.mixer_music.load("Sounds/Win_Sound.mp3")
    p.mixer_music.play()
    endwinwrap = c.CTkFrame(app, fg_color="#eb3ba3", corner_radius=0)
    endwin = c.CTkLabel(endwinwrap, fg_color="#0681B1", corner_radius=0)
    Win = c.CTkImage(light_image=Image.open("Images/You_Win.png"), size=(500, 500))

    winImg = c.CTkLabel(endwin, image=Win, text="", compound="top")

    endwinwrap.place(relwidth=1, relheight=0.75, relx=0.5, rely=0.5, anchor="center")
    endwin.place(relwidth=1, relheight=0.95, relx=0.5, rely=0.5, anchor="center")
    winImg.place(relx=0.5, rely=0.5, anchor="center")
# ***************************************************************************#


# ***********************************LOSE************************************#
def lose_screen():
    p.mixer_music.load("Sounds/Lose_Sound.mp3")
    p.mixer_music.play()
    endlosewrap = c.CTkFrame(app, fg_color="#FF6B6B", corner_radius=0)
    endlose = c.CTkLabel(endlosewrap, fg_color="#0681B1", corner_radius=0)
    Lose = c.CTkImage(light_image=Image.open("Images/You_Lose.png"), size=(500, 500))

    loseImg = c.CTkLabel(endlose, image=Lose, text="", compound="top")

    endlosewrap.place(relwidth=1, relheight=0.75, relx=0.5, rely=0.5, anchor="center")
    endlose.place(relwidth=1, relheight=0.95, relx=0.5, rely=0.5, anchor="center")
    loseImg.place(rely=0.5, relx=0.5, anchor="center")
# ***************************************************************************#


app.mainloop()
