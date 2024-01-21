# *****************************EXTERNAL-MODULES*******************************#

#********DEPENDENCIES******#
# pip install customtkinter
# pip install Pillow
# pip install pygame
#**************************#

import customtkinter as c
from PIL import Image
import pygame as p
# ****************************************************************************#


# ***************************************APP**********************************#
app = c.CTk(fg_color="#298aae")
app.geometry("1200x850")
app.title("Blackjack Mini Project")
app.iconbitmap("Images/Blackjack.ico")
# app.attributes('-fullscreen', True)
p.mixer.init()
# ****************************************************************************#


# *****************************USER-DEFINED-MODULES***************************#
from Animation import *
from Image import *
import Cards as C
import Variables as v

from Pick import *
from Hit_Stand import *

from Refresh import card_refresh
from Initial_Deal import initial_card_deal
from User_Hit import user_hit
from Bot_Logic import bot_logic

# ****************************************************************************#


# ******************************FUNCTIONS*************************************#
# Start the game
def start():
    p.mixer_music.load("Sounds/Start_Button_Sound.mp3")
    p.mixer_music.play()
    gamespace("inplay")
    home.pack_forget()
    initial_card_deal(v.n)
    bot_logic()


#Rules page
def howtoplay():
    p.mixer_music.load("Sounds/Stand_Clicking_Sound.mp3")
    p.mixer_music.play()
    home.pack_forget()
    rules.pack()


#Return to homepage
def back():
    p.mixer_music.load("Sounds/Stand_Clicking_Sound.mp3")
    p.mixer_music.play()
    rules.pack_forget()
    home.pack()

# Hit by user
def main_user_hit():
    p.mixer_music.load("Sounds/Card_Drawn_Sound.mp3")
    p.mixer_music.play()
    user_hit()
    user = int(v.user_hand.get())
    dealer = int(v.dealer_hand.get())
    if user > 21:
        main_stand(user, dealer)


#Stand functionality
def main_stand(user, dealer):
    p.mixer_music.load("Sounds/Stand_Clicking_Sound.mp3")
    p.mixer_music.play()
    stand(user, dealer)
    tok = int(v.token.get())
    if tok > 50:
        v.token.set(50)
    gamespace("end")


#Round end sequence
def round_end():
    p.mixer_music.load("Sounds/Card_Drawn_Sound.mp3")
    p.mixer_music.play()
    global card_num, bot_card_num, n
    if int(v.token.get()) == 50:
        app.configure(fg_color="#292F36")
        win_screen()
        game["end"].pack_forget()
        return
    elif int(v.token.get()) == 0:
        app.configure(fg_color="#292F36")
        lose_screen()
        game["end"].pack_forget()
        return
    v.card_num = 1
    v.bot_card_num = 1
    for i in range(1, 6):
        v.bot_card_lst[i].set("")
        v.card_lst[i].set("")
    card_refresh()
    v.n += 2
    gamespace("inplay")
    game["end"].pack_forget()
    initial_card_deal(v.n)
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

howtoplay = c.CTkButton(
    home,
    corner_radius=24,
    font=c.CTkFont(family="Arial Rounded MT Bold", size=46, weight="bold"),
    text_color="#F5F0F6",
    text="HOW TO PLAY?",
    fg_color="#045676",
    hover_color="#1A4C60",
    command=howtoplay
)

home.pack()
logo_label.place(rely=0.18, relx=0.5, anchor="center")
start.place(rely=0.6, relx=0.5, anchor="center")
howtoplay.place(rely=0.75, relx=0.5, anchor="center")
# ***************************************************************************#


# *****************************RULES-PAGE************************************#
fontheading = c.CTkFont(family="Corbel", size=68, slant="italic", weight="bold", underline = "True")

fontmain = c.CTkFont(family="Comic Sans MS", size=30, weight="bold")

wid = app.winfo_screenwidth()
heig = app.winfo_screenheight()

rules = c.CTkFrame(app, fg_color="#298aae", height=heig, width=wid)

Back = c.CTkButton(
    rules,
    corner_radius=24,
    font=c.CTkFont(family="Arial Rounded MT Bold", size=66, weight="bold"),
    text_color="#F5F0F6",
    text="BACK",
    fg_color="#045676",
    hover_color="#1A4C60",
    command=back
)

logo_label = c.CTkLabel(
    rules,
    font=fontheading,
    text_color="#FECD48",
    text=" How to Play ",
)

Serial = c.CTkLabel(
    rules,
    font=fontmain,
    text_color="#FFFFFF",
    text="1)\n\n2)\n\n\n3)\n\n\n4)\n\n\n5)\n\n\n6)\n\n\n7)",
    justify="left"
)

Rules = c.CTkLabel(
    rules,
    font=fontmain,
    text_color="#FFFFFF",
    text="The game consists of multiple rounds.\n\nThe objective of the user in each round is to get a score close to or equal to 21 using the cards in hand. "
        "If the score exceeds 21, you lose the round.\n\nNumbered cards have a value equal to their face value, irrespective of the suit of the card. "
        "Jack, King, Queen = 10 and Ace can either be 1 or 11 depending on the score of that round.\n\nYou will start each round with 2 cards drawn and your "
        "score shown. The bot's score will not be revealed until the round ends.\n\nBased on your score, you may chose to add a card from the card pile to increase "
        "your score or chose to 'stand' with your current score.\n\nIf you win the round, your points get doubled. If you lose the round, your "
        "points get halved.\n\n\nIf your token count reaches or crosses 50, you WIN the game. If it becomes 0 you LOSE the game. ALL THE BEST!!!",
    wraplength=wid-320,
    justify="left"
)


Back.place(rely=0.06, relx=0.12, anchor="center")
logo_label.place(rely=0.06, relx=0.5, anchor="center")

Serial.place(rely=0.16, relx=0.1, anchor="nw")
Rules.place(rely=0.16, relx=0.13, anchor="nw")
# ***************************************************************************#


# *****************************GAMESPACE*************************************#
game = {"inplay": None, "end": None}


def gamespace(screen):
    global blank

    v.dealer_hand_show.set(value="?")

    wid = app.winfo_screenwidth()
    heig = app.winfo_screenheight()

    game[screen] = c.CTkFrame(app, fg_color="#0681B1", width=wid, height=heig)

    if screen == "end":
        v.dealer_hand_show.set(value=v.dealer_hand.get())

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
            border_color="#CB9501",
        )

        result = c.CTkLabel(
            game[screen],
            textvariable=v.round_result,
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
        command=main_user_hit,
        fg_color="transparent",
        hover="false",
    )

    stand_but = c.CTkButton(
        game[screen],
        corner_radius=12,
        font=c.CTkFont(family="Arial Rounded MT Bold", size=48, weight="bold"),
        text_color="#C5FE9A",
        text="STAND",
        fg_color="#045676",
        hover_color="#1A4C60",
        command=lambda: main_stand(int(v.user_hand.get()), int(v.dealer_hand.get())),
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
        textvariable=v.token,
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

    v.user_card[1] = c.CTkLabel(
        game[screen],
        text="",
        textvariable=v.card_lst[0],
        image=None,
        font=c.CTkFont(size=192),
        text_color="#000000",
        fg_color="transparent",
        bg_color="transparent",
    )

    v.user_card[2] = c.CTkLabel(
        game[screen],
        text="",
        textvariable=v.card_lst[0],
        image=None,
        font=c.CTkFont(size=192),
        text_color="#000000",
    )

    v.user_card[3] = c.CTkLabel(
        game[screen],
        text="",
        textvariable=v.card_lst[0],
        image=None,
        font=c.CTkFont(size=192),
        text_color="#000000",
    )

    v.user_card[4] = c.CTkLabel(
        game[screen],
        text="",
        textvariable=v.card_lst[0],
        image=None,
        font=c.CTkFont(size=192),
        text_color="#000000",
    )

    v.user_card[5] = c.CTkLabel(
        game[screen],
        text="",
        textvariable=v.card_lst[0],
        image=None,
        font=c.CTkFont(size=192),
        text_color="#000000",
    )

    user_name = c.CTkLabel(
        game[screen],
        text="😃 YOU",
        font=c.CTkFont(family="Comic Sans MS", size=42, weight="bold"),
        text_color="#010010",
    )

    user_score = c.CTkButton(
        game[screen],
        textvariable=v.user_hand,
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

    v.bot_card[1] = c.CTkLabel(
        game[screen],
        text="",
        textvariable=v.bot_card_lst[0],
        image=card_design,
        font=c.CTkFont(size=192),
        text_color="#000000",
    )

    v.bot_card[2] = c.CTkLabel(
        game[screen],
        text="",
        textvariable=v.bot_card_lst[0],
        image=card_design,
        font=c.CTkFont(size=192),
        text_color="#000000",
    )

    v.bot_card[3] = c.CTkLabel(
        game[screen],
        text="",
        textvariable=v.bot_card_lst[0],
        image=card_design,
        font=c.CTkFont(size=192),
        text_color="#000000",
    )

    v.bot_card[4] = c.CTkLabel(
        game[screen],
        text="",
        textvariable=v.bot_card_lst[0],
        image=card_design,
        font=c.CTkFont(size=192),
        text_color="#000000",
    )

    v.bot_card[5] = c.CTkLabel(
        game[screen],
        text="",
        textvariable=v.bot_card_lst[0],
        image=card_design,
        font=c.CTkFont(size=192),
        text_color="#000000",
    )

    bot_name = c.CTkLabel(
        game[screen],
        text="🤖 BOT",
        font=c.CTkFont(family="Comic Sans MS", size=42, weight="bold"),
        text_color="#FEFFFE",
    )

    bot_score = c.CTkButton(
        game[screen],
        textvariable=v.dealer_hand_show,
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
    v.user_card[1].place(rely=0.795, relx=0.3, anchor="center")
    v.user_card[2].place(rely=0.795, relx=0.4, anchor="center")
    v.user_card[3].place(rely=0.795, relx=0.5, anchor="center")
    v.user_card[4].place(rely=0.795, relx=0.6, anchor="center")
    v.user_card[5].place(rely=0.795, relx=0.7, anchor="center")
    user_name.place(rely=0.95, relx=0.5, anchor="center")
    v.bot_card[1].place(rely=0.2, relx=0.3, anchor="center")
    v.bot_card[2].place(rely=0.2, relx=0.4, anchor="center")
    v.bot_card[3].place(rely=0.2, relx=0.5, anchor="center")
    v.bot_card[4].place(rely=0.2, relx=0.6, anchor="center")
    v.bot_card[5].place(rely=0.2, relx=0.7, anchor="center")
    bot_name.place(rely=0.05, relx=0.5, anchor="center")

    if screen == "end":
        stand_but.configure(state="disabled")
        card_stack.configure(state="disabled")
        if int(v.token.get()) == 50 or int(v.token.get()) == 0:
            next_round.configure(text="END GAME")
        for i in range(1, 6):
            v.user_card[i].configure(textvariable=v.card_lst[i], image=blank)
            v.bot_card[i].configure(textvariable=v.bot_card_lst[i], image=blank)
# ***************************************************************************#


# *************************************WIN***********************************#
def win_screen():
    p.mixer_music.load("Sounds/Win_Sound.mp3")
    p.mixer_music.play()
    endwinwrap = c.CTkFrame(app, fg_color="#EB3BA3", corner_radius=0)
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
