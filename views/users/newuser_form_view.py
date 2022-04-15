from tkinter import Label, Entry, Button

import window
from controllers import users_controller


def show(message='', error=''):
    root = window.get_clean_root()

    message_label = Label(root, text='')
    if message != '':
        message_label = Label(root, text=f'{message}', fg='green')
    elif error != '':
        message_label = Label(root, text=f'{error}', fg='red')
    message_label.grid(row=0, column=0)

    Label(root, text="Add new user").grid(row=1, column=0, columnspan=2, padx=10, pady=10)
    Label(root, text='New user username:').grid(row=2, column=0)
    username_entry = Entry(root, width=40)
    username_entry.grid(row=2, column=1)

    Button(root,
           text='Add',
           command=lambda: users_controller.add_user_handler(
               username_entry.get())
           ).grid(row=3, column=0, columnspan=2)

    Button(root, text="Back", command=lambda: users_controller.list()).grid(row=4, column=0, columnspan=2)
