import tkinter as tk
import time
from math import sin, cos, radians
W = 500

root = tk.Tk()
canvas = tk.Canvas(width=W, height=W, bg='white')
canvas.pack(padx=20, pady=20)
label = tk.Label(width=20, font=('Times New Roman', 20))
label.pack()
canvas.create_oval(W*0.1, W*0.1, W*0.9, W*0.9)
canvas.create_oval(W/2-5, W/2-5, W/2+5, W/2+5)
hand = canvas.create_line(W/2, W/2, W/2, W*0.2, fill='green', width=3)

def draw_hand(t):
    t = t % 60
    angle = 360 / 60 * t - 90
    dx = 0.3 * W * cos(radians(angle))
    dy = 0.3 * W * sin(radians(angle))
    canvas.coords(hand, W/2, W/2, W/2+dx, W/2+dy)

t1 = time.time()
while True:
    t2 = time.time()
    t = t2 - t1
    sec = int(t % 60)
    minutes = int(t // 60)
    label.config(text=f'{minutes}:{sec:0>2}')
    root.update()
    time.sleep(0.05)
    draw_hand(t)

root.mainloop()