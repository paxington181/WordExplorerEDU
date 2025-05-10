import random
import tkinter as tk
from tkinter import *
from tkinter import ttk


KEYBOARD = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m", "'", "-"]


back_ground = "darkgray"
button_colour = "lightgray"
button_background = {}

def read_wordlist():
    pass

def random_word():
    pass

def get_definition():
    pass

def button_background_builder():
    for key in KEYBOARD:
        button_background[key] = button_colour
    return button_background

button_background_builder()

def add_letter(let):
    current_text = word_entry.get()
    word_entry.delete(0, tk.END)
    word_entry.insert(0, current_text + let)

def clear_entry():
    word_entry.delete(0, tk.END)    



word_to_guess = "placeholder" #Call random_word
word_definition = "Placeholder text that will be later filled with a definition once I go from rigging my UI to making the UI pretty" #Get definition from defition list

main_window = tk.Tk()
main_window.geometry("900x400")
main_window.configure(bg = back_ground)
main_window.title("Word Explorer")

guess_box = Listbox(main_window)
guess_box.grid(row = 0, column = 1)

word_definition_text = Text(main_window, height = 4, width = 30, bg = button_colour)
word_definition_text.grid(row = 0, column = 2)
word_definition_text.insert(tk.END, word_definition)

letters_wrong_place = Listbox(main_window)
letters_wrong_place.grid(row = 0, column = 3)

wrong_letters = Listbox(main_window)
wrong_letters.grid(row = 0, column = 4)

Label(main_window, bg = back_ground, text = "Guess").grid(row = 1, column = 2)
word_entry = Entry(main_window)
word_entry.grid(row = 1, column = 3)

submit_button = tk.Button(main_window, bg = button_colour, text = "Guess word", width = 10)
submit_button.grid(row = 2, column = 2)

clear_button = tk.Button(main_window, bg = button_colour, text = "Clear", width = 10, command = clear_entry)
clear_button.grid(row = 2, column = 3)

keyboard_frame = tk.Frame(main_window, bg = back_ground)
keyboard_frame.grid(row = 3, column = 0, columnspan = 5)
keycolumn = 0
keyrow = 0
for key in KEYBOARD:
    key = tk.Button(keyboard_frame, bg = button_background[key], text = key, width = 1, command = lambda k = key: add_letter(k))
    key.grid(row = keyrow, column = keycolumn, padx = 5, pady = 5)
    if keycolumn < 10 and keyrow == 0:
        keycolumn += 1
        if keycolumn == 10:
            keyrow += 1
            keycolumn = 0
    elif keycolumn < 9 and keyrow == 1:
        keycolumn += 1
        if keycolumn == 9:
            keyrow += 1
            keycolumn = 0
    elif keyrow == 2:
        keycolumn += 1



main_window.mainloop()
