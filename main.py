import tkinter as tk
from tkinter import *
from tkinter import ttk

import random


main_window = tk.Tk()
main_window.title("Word Explorer")

menu = Menu(main_window)
main_window.config(menu = menu)
help_menu = Menu(main_window)
menu.add_cascade(label = "Help", menu = help_menu)
help_menu.add_command(label = "About")



main_window.mainloop()
