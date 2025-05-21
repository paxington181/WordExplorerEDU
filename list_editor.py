import tkinter as tk
from tkinter import *
word_list = []
definition_list = []

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

def remove_line(word_entry):
    pass

#Builds the main window
main_window = tk.Tk()
main_window.configure(bg = "lightgrey")
main_window.title("Word Explorer")

#Adds buttons to makes changes to the whole list with a single click
mb_frame = LabelFrame(main_window)
mb_frame.grid(row = 0, column = 0)
update_all = Button(mb_frame, text = "Update All")
update_all.grid(row = 0, column = 0)
remove_all = Button(mb_frame, text = "Remove All")
remove_all.grid(row = 0, column = 1)
reset_default = Button(mb_frame, text = "Reset to Default")
reset_default.grid(row = 0, column = 2)

#Generates the word list, definition list, and buttons to modify entries
word_frame = LabelFrame(main_window, text = "Word List")
word_frame.grid(row = 1, column = 0)
for i in range(0, len(word_list)):
    word_box = Entry(word_frame)
    word_box.insert(0, word_list[i])
    word_box.grid(row = i + 1, column = 0)
    definition_box = Entry(word_frame)
    definition_box.insert(0, definition_list[i])
    definition_box.grid(row = i + 1, column = 1)
    update_line = Button(word_frame, text = "Update")
    update_line.grid(row = i + 1, column = 2)
    remove_line = Button(word_frame, text = "Remove")
    remove_line.grid(row = i + 1, column = 3)

#Adds 10 empty rows of entry boxes to add to the word list
for i in range(0, 10):
    word_box = Entry(word_frame)
    word_box.grid(row = i + (len(word_list) + 1), column = 0)
    definition_box = Entry(word_frame)
    definition_box.grid(row = i + (len(word_list) + 1), column = 1)
    save_line = Button(word_frame, text = "Save")
    save_line.grid(row = i + (len(word_list) + 1), column = 2)
    remove_line = Button(word_frame, text = "Remove")
    remove_line.grid(row = i + (len(word_list) + 1), column = 3)

main_window.mainloop()