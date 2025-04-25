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


for key in keyboard1:
    
    _button = tk.Button(main_window, bg = back_ground, text = key, width = 1)
    _button.grid(row = , column = )

main_window.mainloop()
