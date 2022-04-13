from tkinter import *

import window
from controllers import app_controller


def show():
    root = window.get_clean_root()
    login_root_label = Label(root, text="Log in")
    login_label = Label(root, text='Login:')
    login_entry = Entry(root, width=40)
    password_label = Label(root, text='Password:')
    password_entry = Entry(root, width=40)
    logmein_button = Button(root, text='Log me in!',
                            command=lambda: app_controller.login_handler(login_entry.get(), password_entry.get()))

    login_root_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
    login_label.grid(row=1, column=0)
    login_entry.grid(row=1, column=1)
    password_label.grid(row=2, column=0)
    password_entry.grid(row=2, column=1)
    logmein_button.grid(row=3, column=0, columnspan=2)
