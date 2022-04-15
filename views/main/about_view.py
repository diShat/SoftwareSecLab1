from tkinter import *
import window
from controllers import app_controller


def show():
    root = window.get_clean_root()

    Label(root,
          text="""Програма виконана студенткою групи ФБ-92 Шатковською Діаною\n
          Варіант 13: Наявність букв, розділового знаку і знаків арифметичних операцій."""
          ).grid(row=1, column=0, columnspan=2)

    backtomain_btn = Button(root, text="Back", command=lambda: app_controller.main())
    backtomain_btn.grid(row=6, column=0, columnspan=2)
