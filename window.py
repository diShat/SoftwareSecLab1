from tkinter import *

global root
root = Tk()
root.title("SoftwareSecurity-Lab1")
root.minsize(300, 30)


def get_clean_root():
    if len(root.winfo_children()) != 0:
        for el in root.winfo_children():
            el.destroy()
    return root
