import tkinter as tk

root = tk.Tk()
root.title('Radiobuttons')
FONT = ('Courier', 30)
W = 300
COLORS = {1: 'red', 2: 'green', 3: 'blue'}

color_number = tk.IntVar()
color_number.set(1)

r1 = tk.Radiobutton(root, text='red', font=FONT,
                    variable=color_number, value=1)
r1.grid(row=0, column=0, sticky='w')
r2 = tk.Radiobutton(root, text='green', font=FONT,
                    variable=color_number, value=2)
r2.grid(row=1, column=0, sticky='w')
r3 = tk.Radiobutton(root, text='blue', font=FONT,
                    variable=color_number, value=3)
r3.grid(row=2, column=0, sticky='w')
canvas = tk.Canvas(root, bg='white', width=W, height=W)
canvas.grid(row=0, column=1, rowspan=4)

def click():
    # if color_number.get() == 1:
    #     canvas.config(bg='red')
    # if color_number.get() == 2:
    #     canvas.config(bg='green')
    # if color_number.get() == 3:
    #     canvas.config(bg='blue')
    canvas.delete('all')
    canvas.config(bg=COLORS.get(color_number.get()))
    if is_circle.get():
        canvas.create_oval(5, 5, W//3, W//3, fill='black')

btn = tk.Button(root, text='Color', command=click, font=FONT)
btn.grid(row=3, column=0)

is_circle = tk.BooleanVar()
is_circle.set(False)
check1 = tk.Checkbutton(root, text='circle', font=FONT,
                        variable=is_circle,
                        onvalue=True, offvalue=False)
check1.grid(row=0, column=2)

root.mainloop()