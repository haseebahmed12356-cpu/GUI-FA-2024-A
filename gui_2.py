import tkinter as tk

import login

window = tk.Tk()
window.geometry("400x400")

window.title("Login")
# Username
label_username = tk.Label(window,text="Username")
label_username_entry = tk.Entry(window,width=20)
label_username.pack()
label_username_entry.pack()

# Password
label_password = tk.Label(window,text="Password")
label_password_entry = tk.Entry(window,width=20)
label_password.pack()
label_password_entry.pack()

def login():
    if(label_username_entry.get() == 'subhan') & (label_password_entry.get() == '123'):
        # print('Login Successful')
        label_message.config(text='Login Successful')
        button_password.config(bg='green')
    else:
        # print('Login Unsuccessful')
        label_message.config(text='Login Unsuccessful', fg='red')
        button_password.config(bg='red')

button_password = tk.Button(window,text="Login",command=login)
button_password.pack()


# Message
label_message = tk.Label(window,text="")
label_message.pack()

window.mainloop()