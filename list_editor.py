#Imports tkinterface to be able to build the GUI
import tkinter as tk
from tkinter import *
import json

#Variables that are needed across the entire program
wordlist = {}

#Imports the default wordlist from a json file
with open("default_wordlist.json", "r") as file:
    wordlist = json.load(file)

#Functions that are called when the buttons are pressed


def update_line():
    pass

def update_all():
    pass

def remove_line():
    pass

def remove_all():
    pass


def save_line():
    pass

#Removes the current wordlist, and replaces it with the default wordlist
def reset_default():
    pass

#Builds the main window
main_window = tk.Tk()
main_window.configure(bg = "lightgrey")
main_window.title("Word Explorer")

#Adds buttons to makes changes to the whole list with a single click
mb_frame = LabelFrame(main_window)
mb_frame.pack()
update_all = Button(mb_frame, text = "Update All")
update_all.grid(row = 0, column = 0)
remove_all = Button(mb_frame, text = "Remove All")
remove_all.grid(row = 0, column = 1)
reset_default = Button(mb_frame, text = "Reset to Default")
reset_default.grid(row = 0, column = 2)

#Entry fields for adding words and definitions to the list
add_frame = LabelFrame(main_window, text = "Add Word", padx = 10)
add_frame.pack()
word_entry = Entry(add_frame)
word_entry.grid(row = 0, column = 0)
definition_entry = Entry(add_frame, width = 100)
definition_entry.grid(row = 0, column = 1)
add_word = Button(add_frame, text = "Add Word", padx = 10)
add_word.grid(row = 0, column = 2)
clear_entry = Button(add_frame, text = "Clear Entries")
clear_entry.grid(row = 0, column = 3)

#Generates boxes for the word list, definition list, and buttons to modify entries
word_frame = LabelFrame(main_window, text = "Word List")
word_frame.pack()
i = 0
for key, value in wordlist.items():
    word_box = Entry(word_frame)
    word_box.insert(0, key)
    word_box.grid(row = i, column = 0)
    definition_box = Entry(word_frame, width = 100)
    definition_box.insert(0, value)
    definition_box.grid(row = i, column = 1)
    update_line = Button(word_frame, text = "Update")
    update_line.grid(row = i, column = 2)
    remove_line = Button(word_frame, text = "Remove")
    remove_line.grid(row = i, column = 3)
    i += 1
    


main_window.mainloop()