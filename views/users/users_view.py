from tkinter import *
from tkinter import ttk

import window
from controllers import users_controller


def show(users):
    root = window.get_clean_root()

    headers = ['Id', 'Username', 'Admin', 'Blocked', 'Pass Restricted']
    for i, header in enumerate(headers):
        Label(root, text=f'{header}').grid(row=0, column=i)

    for row, user in enumerate(users):
        Label(root, text=f'{user.id}').grid(row=row+1, column=0)
        Label(root, text=f'{user.username}').grid(row=row+1, column=1)
        Label(root, text=f'{user.is_admin}').grid(row=row+1, column=2)
        Label(root, text=f'{user.is_blocked}').grid(row=row+1, column=3)
        Label(root, text=f'{user.is_pass_restricted}').grid(row=row+1, column=4)

        Button(
            root,
            text="Unblock" if user.is_blocked else 'Block',
            command=lambda user=(user.username, user.is_blocked): users_controller.set_block_status_handler(
                user[0],
                not user[1]
            )
        ).grid(row=row + 1, column=5)