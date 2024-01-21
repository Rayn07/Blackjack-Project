import customtkinter as c


app = c.CTk()
app.geometry('800x550')
app.attributes('-fullscreen', True)


movex = 0
movey = 0

img = c.

def move():
    global movex, movey
    movex += 0.002
    movey += 0.002
    label.place_configure(relx=movex,rely=movey, anchor='center')
    if not movex > 0.5:
        label.after(1, move)

label = c.CTkLabel(app, text="O", font=c.CTkFont(size=200))
label.place(relx='0', rely='0')

move()

app.mainloop()