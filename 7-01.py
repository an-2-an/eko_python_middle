import tkinter as tk

FONT = ("Courier", 26)

root = tk.Tk()

box = tk.Listbox(root, width=5, height=10, font=FONT,
                 selectmode=tk.MULTIPLE)
for i in range(10, 101, 10):
    box.insert('end', i)
box.pack()

label = tk.Label(root, width=30,
                 font=FONT, bg='black', fg='white')
label.pack()

def click():
    ind = box.curselection()
    vals = [box.get(i) for i in ind]
    s = '+'.join(str(v) for v in vals) + '=' + str(sum(vals))
    label.config(text=s)

button = tk.Button(root, text='Cумма чисел',
                command=click, font=FONT)
button.pack()

root.mainloop()