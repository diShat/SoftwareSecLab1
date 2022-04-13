from tkinter import *

global root
root = Tk()
root.geometry('800x600')


def get_clean_root():
    if len(root.winfo_children()) != 0:
        for el in root.winfo_children():
            el.destroy()
    return root
