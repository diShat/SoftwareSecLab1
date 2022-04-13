from tkinter import Label

import window


def show(users):
    root = window.get_clean_root()
    Label(root, text=f"Users:").grid(row=0, column=0)
    Label(root, text=f"Users:").grid(row=0, column=0)
    for i, user in enumerate(users):
        Label(root, text=f"{user.username}").grid(row=i+2, column=0)
