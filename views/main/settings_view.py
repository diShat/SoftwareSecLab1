from tkinter import *
import window
from controllers import app_controller


def show(username, message='', error=''):
    root = window.get_clean_root()

    message_label = Label(root, text='')
    if message != '': message_label = Label(root, text=f'{message}', fg='green')
    elif error != '': message_label = Label(root, text=f'{error}', fg='red')
    message_label.grid(row=0, column=0)

    login_label = Label(root, text=f"Login: {username}")
    oldpass_label = Label(root, text='Old password:')
    oldpass_entry = Entry(root, width=50)
    newpass_label = Label(root, text='New password:')
    newpass_entry = Entry(root, width=50)
    newpassconf_label = Label(root, text='Confirm new password:')
    newpassconf_entry = Entry(root, width=50)
    changepass_btn = Button(root, text="Change password",
                            command=lambda: app_controller.changepass_handler(oldpass_entry.get(),
                                                                              newpass_entry.get(),
                                                                              newpassconf_entry.get()))

    login_label.grid(row=1, column=0)
    oldpass_label.grid(row=2, column=0)
    oldpass_entry.grid(row=2, column=1)
    newpass_label.grid(row=3, column=0)
    newpass_entry.grid(row=3, column=1)
    newpassconf_label.grid(row=4, column=0)
    newpassconf_entry.grid(row=4, column=1)
    changepass_btn.grid(row=5, column=0, columnspan=2)

    backtomain_btn = Button(root, text="Back", command=lambda: app_controller.main())
    backtomain_btn.grid(row=6, column=0, columnspan=2)
