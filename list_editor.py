#Imports tkinterface to be able to build the GUI
import tkinter as tk
from tkinter import *

#Variables that are needed across the entire program
word_list = []
definition_list = []

#The main function that builds the list for the GUI assembly
def main():

#Reads the wordlist file, removes comments and then adds the words and definitions to their lists without the prefixes.    
    with open("wordlist.txt") as file:
        unmodified_wordlist = file.read().splitlines()
        for line in unmodified_wordlist:
            if line.startswith("#"):
                unmodified_wordlist.remove(line)
            elif line.startswith("w."):
                word_list.append(line[2:])
            elif line.startswith("d."):
                definition_list.append(line[2:])

main()

#Functions that are called when the buttons are pressed
def update_line():
    pass

def update_all():
    pass

def remove_line(word_entry):
    pass

def remove_all():
    pass


def save_line(word_entry):
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
for i in range(0, len(word_list)):
    word_box = Entry(word_frame)
    word_box.insert(0, word_list[i])
    word_box.grid(row = i + 1, column = 0)
    definition_box = Entry(word_frame, width = 100)
    definition_box.insert(0, definition_list[i])
    definition_box.grid(row = i + 1, column = 1)
    update_line = Button(word_frame, text = "Update")
    update_line.grid(row = i + 1, column = 2)
    remove_line = Button(word_frame, text = "Remove")
    remove_line.grid(row = i + 1, column = 3)


main_window.mainloop()