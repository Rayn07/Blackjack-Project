from PIL import Image
import customtkinter as c

movex, movey = 0, 0

card_design = c.CTkImage(
    light_image=Image.open("Images/Card_Design.jpg"),
    size=(105, 160),
)

blank = c.CTkImage(
    light_image=Image.open("Images/Blank.png")
)

def animation(x, y, label, n, card_lst):
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
            label.configure(textvariable=card_lst[n], image=blank)
            label.place_configure(relx=eval(x),rely=eval(y), anchor='center')
    move()