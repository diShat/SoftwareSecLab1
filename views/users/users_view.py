from tkinter import *

import window
from controllers import users_controller, app_controller


def show(users):
    root = window.get_clean_root()

    # creating management menu
    backtomain_btn = Button(root, text="Back", command=lambda: app_controller.main())
    backtomain_btn.grid(row=0, column=0)

    # drawing a users-table
    headers = ['Id', 'Username', 'Admin', 'Blocked', 'Pass Restricted']
    for i, header in enumerate(headers):
        Label(root, text=f'{header}').grid(row=1, column=i)

    for row, user in enumerate(users):
        Label(root, text=f'{user.id}').grid(row=row+2, column=0)
        Label(root, text=f'{user.username}').grid(row=row+2, column=1)
        Label(root, text=f'{user.is_admin}').grid(row=row+2, column=2)
        Label(root, text=f'{user.is_blocked}').grid(row=row+2, column=3)
        Label(root, text=f'{user.is_pass_restricted}').grid(row=row+2, column=4)

        if not user.is_admin:
            Button(
                root,
                text="Unblock" if user.is_blocked else 'Block',
                command=lambda u=(user.username, user.is_blocked): users_controller.set_block_status_handler(
                    u[0],
                    not u[1]
                )
            ).grid(row=row+2, column=5)

            Button(
                root,
                text="Unrestrict" if user.is_pass_restricted else 'Restrict',
                command=lambda u=(user.username, user.is_pass_restricted): users_controller.set_restrict_status_handler(
                    u[0],
                    not u[1]
                )
            ).grid(row=row+2, column=6)
