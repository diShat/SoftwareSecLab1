from tkinter import Label, Entry, Button

import window
from controllers import users_controller


def show():
    root = window.get_clean_root()
    Label(root, text="Add new user").grid(row=0, column=0, columnspan=2, padx=10, pady=10)
    Label(root, text='New user username:').grid(row=1, column=0)
    username_entry = Entry(root, width=40)
    username_entry.grid(row=1, column=1)

    Button(root,
           text='Add',
           command=lambda: users_controller.add_user_handler(
               username_entry.get())
           ).grid(row=2, column=0, columnspan=2)
