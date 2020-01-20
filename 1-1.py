import tkinter as tk
import random

root = tk.Tk()
xt, yt = random.randint(50, 550), random.randint(50, 550) #клад
counter = 0

canvas = tk.Canvas(width=600, height=600, bg='#aaaaaa')
canvas.pack(padx=20, pady=20)
label = tk.Label(width=20, font=('Times New Roman', 20))
label.pack()

def distance(x, y):
    return int(((x-xt)**2 + (y-yt)**2) ** 0.5)

def click(e):
    global counter
    x, y = e.x, e.y
    if counter >= 7:
        canvas.create_text(300, 300, text='Попытки закончились', font=('Times New Roman', 30))
    else:
        d = distance(x, y)
        label.config(text=str(d))
        canvas.create_text(x+10, y, text=str(d), fill='white', anchor='w')
        canvas.create_oval(x - 4, y - 4, x + 4, y + 4, fill='red')
        counter += 1
        if d <= 10:
            label.config(text='Победа!!!')
            canvas.create_rectangle(xt - 10, yt - 10, xt + 10, yt + 10, fill='yellow')

canvas.bind('<Button-1>', click)
root.mainloop()