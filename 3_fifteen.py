import random
import tkinter as tk

W = 100

root = tk.Tk()
canvas = tk.Canvas(height=4*W, width=4*W, bg='grey')
canvas.pack(padx=20, pady=20)

captions = '1 2 3 4 5 6 7 8 9 10 11 12 13 14 15'.split() + ['']
random.shuffle(captions)

def draw():
    canvas.delete('all')
    for i in range(1, 4):
        canvas.create_line(0, W*i, W*4, W*i, fill='white')
        canvas.create_line(W*i, 0, W*i, W*4, fill='white')
    for i in range(4):
        for j in range(4):
            canvas.create_text(j*W+W/2, i*W+W/2,
                text=captions[4*i+j], fill='white', font=('Arial', 28))

def click(e):
    global captions
    x, y = e.x, e.y
    row, col = y // W, x // W
    index_click = row * 4 + col
    empty_index = captions.index('')
    # в одноом ряду слева или справа
    if index_click in [empty_index - 1, empty_index + 1] and \
            index_click // 4 == empty_index // 4:
        captions[index_click], captions[empty_index] = \
            captions[empty_index], captions[index_click]
    # в одной колонке сверху или снизу
    if index_click in [empty_index - 4, empty_index + 4]:
        captions[index_click], captions[empty_index] = \
            captions[empty_index], captions[index_click]
    draw()

def cheet(e):
    global captions
    captions = [''] + '2 3 4 1 6 7 8 5 10 11 12 9 13 14 15'.split()
    draw()

draw()
canvas.bind('<Button-1>', click)
canvas.bind('<Button-3>', cheet)
root.mainloop()

'''
доработать пятнашки 
сделать так, чтобы выводилось сообщение
о победе,
когда выигрышная раскладка собрана
'''