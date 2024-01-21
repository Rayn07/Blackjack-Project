from PIL import Image
import customtkinter as c

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





