from tkinter import *
from controllers import app_controller, users_controller
import window


def startup():
    root = window.root
    label = Label(root, text=f"App")
    login_btn = Button(root, text="Log in", command=lambda: app_controller.login())
    label.grid(row=0, column=0)
    login_btn.grid(row=1, column=0)
    root.mainloop()


def show(username, is_admin):
    root = window.get_clean_root()
    login_label = Label(root, text=f"Login: {username}")
    settings_btn = Button(root, text="Settings", command=lambda: app_controller.settings(username))
    userslist_btn = Button(root, text='Show Users list', command=lambda: users_controller.list())
    logout_btn = Button(root, text='Log out', command=lambda: app_controller.login())
    login_label.grid(row=0, column=0)
    settings_btn.grid(row=1, column=0)
    if is_admin: userslist_btn.grid(row=2, column=0)
    logout_btn.grid(row=3, column=0)

