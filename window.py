from tkinter import *

global root
root = Tk()
root.geometry('500x250')


def get_clean_root():
    if len(root.winfo_children()) != 0:
        for el in root.winfo_children():
            el.destroy()
    return root
