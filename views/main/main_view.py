from tkinter import *
from controllers import app_controller, users_controller
import window


def startup():
    root = window.root
    Label(root, text=f"App").grid(row=0, column=0)
    Button(root, text="Log in", command=lambda: app_controller.login()).grid(row=1, column=0)
    root.mainloop()


def show(username, is_admin):
    root = window.get_clean_root()
    Label(root, text=f"You logged in as:: {username}").grid(row=0, column=0)
    Button(root, text="Settings", command=lambda: app_controller.settings()).grid(row=1, column=0)
    if is_admin:
        Button(root, text='Show Users list', command=lambda: users_controller.list()).grid(row=2, column=0)
    Button(root, text="About", command=lambda: app_controller.about()).grid(row=3, column=0)
    Button(root, text='Log out', command=lambda: app_controller.login()).grid(row=4, column=0)

