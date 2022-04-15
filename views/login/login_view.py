from tkinter import *

import window
from controllers import app_controller


def show(message='', error=''):
    root = window.get_clean_root()

    if message != '': Label(root, text=f'{message}', fg='green').grid(row=0, column=0)
    elif error != '': Label(root, text=f'{error}', fg='red').grid(row=0, column=0)
    else: Label(root, text='').grid(row=0, column=0)

    Label(root, text="Log in").grid(row=1, column=0, columnspan=2, padx=5, pady=5)

    Label(root, text='Login:').grid(row=2, column=0)
    login_entry = Entry(root, width=40)
    login_entry.grid(row=2, column=1)

    Label(root, text='Password:').grid(row=3, column=0)
    password_entry = Entry(root, width=40)
    password_entry.grid(row=3, column=1)

    Button(root,
           text='Log me in!',
           command=lambda: app_controller.login_handler(
               login_entry.get(),
               password_entry.get())
           ).grid(row=4, column=0, columnspan=2)
