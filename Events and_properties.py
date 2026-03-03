import tkinter as tk
from tkinter import Tk

window: Tk = tk.Tk()

window.geometry("400x400")

label = tk.Label(window, text="Hello tkinter!",fg='blue',bg='red')

label.pack(padx=10,pady=10)


def change_color():

    current_bg=label.cget('bg')
    label.config(bg=current_bg)

    if current_bg=='red':
        label.config(bg='green')
    elif current_bg=='green':
        label.config(bg='red')

button= tk.Button(window,text="Change color",width=15,command=change_color)




button.pack()
window.mainloop()