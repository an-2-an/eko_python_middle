import tkinter as tk

root = tk.Tk()
root.title('Listbox')
# root.geometry('200x500')

N, W = 10, 300
box = tk.Listbox(root, font=('Arial', 20), height=N, width=5)
for i in range(N):
    box.insert('end', (i + 1)*10)
box.pack(side='left')

def click():
    value = box.get('active')
    # print(value)
    canvas.delete('all')
    side = W*value/100
    canvas.create_rectangle(W//2 - side/2, W//2 - side/2,
                W//2 + side/2, W//2 + side/2, fill='red')
    canvas.create_text(W//2, W//2, text=str(value),
                       fill='white', font=('Arial', 20))

btn = tk.Button(root, font=('Arial', 20), text='Click',
                command=click)
btn.pack(side='left', padx=20)

canvas = tk.Canvas(root, width=W, height=W, bg='black')
canvas.pack(side='left', padx=20)

root.mainloop()