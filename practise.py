import tkinter as tk

def handle_click(event):
    print(f"Button clicked at X={event.x}, Y={event.y}")

def handle_key(event):
    print(f"Key pressed: {event.char}")

window = tk.Tk()
window.geometry("400x300")

button = tk.Button(window, text="Click Me")
button.pack(pady=10)

entry = tk.Entry(window)
entry.pack(pady=10)

# Bind left mouse click on button
button.bind("<Button-1>", handle_click)

# Bind any key press on entry
entry.bind("<Key>", handle_key)

window.mainloop()