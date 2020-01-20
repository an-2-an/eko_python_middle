import tkinter as tk

WIDTH, HEIGHT = 1400, 700
root = tk.Tk()

x, y = 100, 100
r = 20
vx, vy = 5, -5
TIMEOUT = 10
x_pad, d_pad, h_pad = WIDTH // 2, 100, 40
points = 0
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg='grey')
canvas.pack()

points_text = canvas.create_text(WIDTH-5, 5, text='0',
        fill='white', font=('Arial', 30), anchor='ne')

ball = canvas.create_oval(x-r, y-r, x+r, y+r, fill='yellow')
pad = canvas.create_rectangle(x_pad-d_pad, HEIGHT, x_pad+d_pad,
                        HEIGHT-h_pad, fill='green')

def game():
    global x, y, vx, vy, points
    x, y = x+vx, y+vy
    canvas.coords(ball, x-r, y-r, x+r, y+r)
    if y == r:
        vy = -vy
        points += 1
        canvas.itemconfig(points_text, text=str(points))
    if x == r or x == WIDTH - r:
        vx = -vx
    if x_pad-d_pad <= x <= x_pad+d_pad and y == HEIGHT-r-h_pad:
        vy = -vy
    if y == HEIGHT - r:
       canvas.create_text(WIDTH/2, HEIGHT/2, text='GAME OVER',
            fill='red', font=('Arial', 70))
    else:
        root.after(TIMEOUT, game)

def keypress(e):
    global x_pad
    if e.keycode == 37:
        x_pad -= 50
    if e.keycode == 39:
        x_pad += 50
    canvas.coords(pad, x_pad-d_pad, HEIGHT, x_pad+d_pad, HEIGHT-h_pad)

def mousemove(e):
    global x_pad
    x_pad = e.x
    canvas.coords(pad, x_pad - d_pad, HEIGHT, x_pad + d_pad, HEIGHT - h_pad)

game()
root.bind('<Key>', keypress)
canvas.bind('<Motion>', mousemove)
root.mainloop()

'''
Дополнить игру Арканоид, добавив внутрь игрового поля 
несколько прямоугольных блоков,
от которых будет отбиваться мяч
'''