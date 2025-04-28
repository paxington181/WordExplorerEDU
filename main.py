import tkinter as tk
from tkinter import *
from tkinter import ttk

import random

back_ground = "dimgrey"
word_definition = "Placeholder text that will be later filled with a definition once I go from rigging my UI to making the UI actually work"

keyboard1 = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p"]
keyboard2 = ["a", "s", "d", "f", "g", "h", "j", "k", "l"]
keyboard3 = ["z", "x", "c", "v", "b", "n", "m"]

main_window = tk.Tk()
main_window.geometry("800x400")
main_window.configure(bg = back_ground)
main_window.title("Word Explorer")

guess_box = Listbox(main_window)
guess_box.grid(row = 0, column = 1)

word_definition_text = Text(main_window, height = 4, width = 30, bg = back_ground)
word_definition_text.grid(row = 0, column = 2)
word_definition_text.insert(tk.END, word_definition)

Label(main_window, bg = back_ground, text = "Guess").grid(row = 1, column = 2)
word_entry = Entry(main_window)
word_entry.grid(row = 1, column = 3)

submit_button = tk.Button(main_window, bg = back_ground, text = "Guess word", width = 10)
submit_button.grid(row = 2, column = 2)

column1 = 0
for key in keyboard1:
    key = tk.Button(main_window, bg = back_ground, text = key, width = 1)
    key.grid(row = 3, column = column1)
    column1 += 1

column2 = 0
for key2 in keyboard2:
    key2 = tk.Button(main_window, bg = back_ground, text = key2, width = 1)
    key2.grid(row = 4, column = column2)
    column2 += 1

column3 = 0
for key3 in keyboard3:
    key3 = tk.Button(main_window, bg = back_ground, text = key3, width = 1)
    key3.grid(row = 5, column = column3)
    column3 += 1

main_window.mainloop()
