# pip install customtkinter
# pip install Pillow
import customtkinter as c
from PIL import Image
import pygame as p


# ******************************FUNCTIONS*************************************#
def start():
    p.mixer_music.load("Sounds/Start_Button_Sound.mp3")
    p.mixer_music.play()
    home.pack_forget()
    game.pack()

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

def ret():
    global token
    count = int(token.get())
    token.set(count + 1)

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

    app.configure(fg_color="#292F36")
    game.pack_forget()

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

    app.configure(fg_color="#292F36")
    game.pack_forget()


# ****************************************************************************#


# *****************************APP-ATTRIBUTES*********************************#
app = c.CTk(fg_color="#0681B1")
app.geometry("1200x850")
app.title("Blackjack Mini Project")
app.iconbitmap("Images/Blackjack.ico")
# app.attributes('-fullscreen', True)
p.mixer.init()
# ****************************************************************************#


# ****************************VARIABLES***************************************#
token = c.StringVar(value=0)

user_score = c.StringVar(value=10)

bot_score = c.StringVar(value=19)
# ****************************************************************************#


# *****************************HOMEPAGE***************************************#
font = c.CTkFont(family="Corbel", size=48, slant="italic", weight="bold")

wid = app.winfo_screenwidth()
heig = app.winfo_screenheight()

home = c.CTkFrame(app, fg_color="#0681B1", height=heig, width=wid)

logo = c.CTkImage(
    light_image=Image.open("Images/Blackjack_Logo.png"),
    size=(760, 220)
)
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

rules = c.CTkFrame(app, fg_color="#0681B1", height=heig, width=wid)

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
stack = c.CTkImage(
    light_image=Image.open("Images/Card_Stack.png"),
    size=(205, 170),
)
card_design = c.CTkImage(
    light_image=Image.open("Images/Card_Design.jpg"),
    size=(105, 160),
)



wid = app.winfo_screenwidth()
heig = app.winfo_screenheight()

game = c.CTkFrame(app, fg_color="#0681B1", width=wid, height=heig)

card_stack = c.CTkButton(
    game,
    image=stack,
    text="",
    command=ret,
    fg_color="transparent",
    hover="false"
)

stand = c.CTkButton(
    game,
    corner_radius=12,
    font=c.CTkFont(family="Arial Rounded MT Bold", size=48, weight="bold"),
    text_color="#C5FE9A",
    text="STAND",
    fg_color="#05648A",
    hover_color="#045676",
    command=ret,
    height=64,
)

Win_Optional = c.CTkButton(
    game,
    corner_radius=12,
    font=c.CTkFont(family="Arial Rounded MT Bold", size=28, weight="bold"),
    text_color="black",
    text="You Win (NOT in actual game)",
    fg_color="#05648A",
    hover_color="#045676",
    command=win_screen,
    height=64,
)

Lose_Optional = c.CTkButton(
    game,
    corner_radius=12,
    font=c.CTkFont(family="Arial Rounded MT Bold", size=28, weight="bold"),
    text_color="black",
    text="You Lose (NOT in actual game)",
    fg_color="#05648A",
    hover_color="#045676",
    command=lose_screen,
    height=64,
)

token_label = c.CTkLabel(
    game,
    text="Tokens",
    font=c.CTkFont(family="Malgun Gothic", size=36, weight="bold"),
    text_color="#EBEBFF",
)

token_counter = c.CTkButton(
    game,
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
    game,
    text="😃 YOU",
    font=c.CTkFont(family="Small Fonts", size=48, weight="bold"),
    text_color="#010010",
)

user_card_1 = c.CTkLabel(
    game,
    text="🂡",
    font=c.CTkFont(size=192),
    text_color="#000000",
)

user_card_2 = c.CTkLabel(
    game,
    text="🂡",
    font=c.CTkFont(size=192),
    text_color="#000000",
)

user_card_3 = c.CTkLabel(
    game,
    text="🂡",
    font=c.CTkFont(size=192),
    text_color="#000000",
)

user_card_4 = c.CTkLabel(
    game,
    text="🂡",
    font=c.CTkFont(size=192),
    text_color="#000000",
)

user_card_5 = c.CTkLabel(
    game,
    text="🂡",
    font=c.CTkFont(size=192),
    text_color="#000000",
)

user_score = c.CTkButton(
    game,
    textvariable=user_score,
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

bot_name = c.CTkLabel(
    game,
    text="🤖 BOT",
    font=c.CTkFont(family="Small Fonts", size=48, weight="bold"),
    text_color="#FEFFFE",
)

bot_card_1 = c.CTkLabel(
    game,
    text="",
    image=card_design,
    font=c.CTkFont(size=192),
    text_color="#000000",
)

bot_card_2 = c.CTkLabel(
    game,
    text="",
    image=card_design,
    font=c.CTkFont(size=192),
    text_color="#000000",
)

bot_card_3 = c.CTkLabel(
    game,
    text="",
    image=card_design,
    font=c.CTkFont(size=192),
    text_color="#000000",
)

bot_card_4 = c.CTkLabel(
    game,
    text="",
    image=card_design,
    font=c.CTkFont(size=192),
    text_color="#000000",
)

bot_card_5 = c.CTkLabel(
    game,
    text="",
    image=card_design,
    font=c.CTkFont(size=192),
    text_color="#000000",
)

bot_score = c.CTkButton(
    game,
    textvariable=bot_score,
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

token_counter.place(rely=0.1, relx=0.1, anchor="center")
token_label.place(rely=0.18, relx=0.1, anchor="center")
stand.place(rely=0.78, relx=0.875, anchor="center")
Win_Optional.place(rely=0.38, relx=0.2, anchor="center")
Lose_Optional.place(rely=0.48, relx=0.2, anchor="center")
user_score.place(rely=0.62, relx=0.5, anchor="center")
bot_score.place(rely=0.385, relx=0.5, anchor="center")
card_stack.place(rely=0.47, relx=0.875, anchor="center")
user_card_1.place(rely=0.795, relx=0.3, anchor="center")
user_card_2.place(rely=0.795, relx=0.4, anchor="center")
user_card_3.place(rely=0.795, relx=0.5, anchor="center")
user_card_4.place(rely=0.795, relx=0.6, anchor="center")
user_card_5.place(rely=0.795, relx=0.7, anchor="center")
user_name.place(rely=0.95, relx=0.5, anchor="center")
bot_card_1.place(rely=0.2, relx=0.3, anchor="center")
bot_card_2.place(rely=0.2, relx=0.4, anchor="center")
bot_card_3.place(rely=0.2, relx=0.5, anchor="center")
bot_card_4.place(rely=0.2, relx=0.6, anchor="center")
bot_card_5.place(rely=0.2, relx=0.7, anchor="center")
bot_name.place(rely=0.05, relx=0.5, anchor="center")
# ***************************************************************************#


app.mainloop()
