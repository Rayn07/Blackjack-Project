# pip install customtkinter
# pip install Pillow
import customtkinter as c
from PIL import Image


# ******************************FUNCTIONS*************************************#
def start():
    home.pack_forget()
    game.pack()


def ret():
    global token
    count = int(token.get())
    token.set(count + 1)


# ****************************************************************************#


# *****************************APP-ATTRIBUTES*********************************#
app = c.CTk(fg_color="#0681B1")
app.geometry("1200x850")
app.title("Blackjack Mini Project")
app.iconbitmap("Images/Blackjack.ico")
# app.attributes('-fullscreen', True)
# ****************************************************************************#


# ****************************VARIABLES***************************************#
token = c.StringVar(value=0)

user_score = c.StringVar(value=10)

bot_score = c.StringVar(value=19)
# ****************************************************************************#


# *****************************HOMEPAGE***************************************#
font = c.CTkFont(family="Corbel", size=48, slant="italic", weight="bold")
logo = c.CTkImage(
    light_image=Image.open("Images/Blackjack_Logo.png"),
    size=(760, 220),
)

home = c.CTkFrame(app, fg_color="#0681B1")

logo_label = c.CTkLabel(
    home,
    image=logo,
    font=font,
    text_color="#FECD48",
    text="Closest to Twent-One",
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

home.pack(fill="both")
logo_label.pack()
start.pack()
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
