import tkinter as tk
from tkinter import *
from tkinter import ttk

import random


main_window = tk.Tk()
main_window.title("Word Explorer")

guess_box = Listbox(main_window)
guess_box.grid(row = 0, column = 1)

word_definition = Text(main_window)

Label(main_window, text = "Guess").grid(row = 1, column = 2)
word_entry = Entry(main_window)
word_entry.grid(row = 1, column = 3)





main_window.mainloop()
