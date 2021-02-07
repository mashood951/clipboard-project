import tkinter as tk

window = tk.Tk()

label = tk.Label(text='Name')
entry = tk.Entry()
name = entry.delete(0)
print(name)

label.pack()
entry.pack()

window.mainloop()