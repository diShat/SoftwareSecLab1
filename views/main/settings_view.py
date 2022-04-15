from tkinter import *
import window
from controllers import app_controller


def show(username, message='', error=''):
    root = window.get_clean_root()

    if message != '': Label(root, text=f'{message}', fg='green').grid(row=0, column=0, columnspan=2)
    elif error != '': Label(root, text=f'{error}', fg='red').grid(row=0, column=0, columnspan=2)
    else: Label(root, text='').grid(row=0, column=0, columnspan=2)

    Label(root, text=f"You logged in as: {username}").grid(row=1, column=0, columnspan=2)

    Label(root, text='Old password:').grid(row=2, column=0)
    oldpass_entry = Entry(root, width=50)
    oldpass_entry.grid(row=2, column=1)

    Label(root, text='New password:').grid(row=3, column=0)
    newpass_entry = Entry(root, width=50)
    newpass_entry.grid(row=3, column=1)

    Label(root, text='Confirm new password:').grid(row=4, column=0)
    newpassconf_entry = Entry(root, width=50)
    newpassconf_entry.grid(row=4, column=1)

    Button(root,
           text="Change password",
           command=lambda: app_controller.changepass_handler(oldpass_entry.get(),
                                                             newpass_entry.get(),
                                                             newpassconf_entry.get())
           ).grid(row=5, column=0, columnspan=2)

    backtomain_btn = Button(root, text="Back", command=lambda: app_controller.main())
    backtomain_btn.grid(row=6, column=0, columnspan=2)
