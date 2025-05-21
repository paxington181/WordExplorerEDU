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


#Checks for duplicates, removes them, and notifies the user


    print(word_list)
    print(len(word_list))   
    print(definition_list)
    print(len(definition_list))

main()

def remove_line(word_entry):
    pass

main_window = tk.Tk()
main_window.geometry("500x400")
main_window.configure(bg = "lightgrey")
main_window.title("Word Explorer")

mb_frame = LabelFrame(main_window)
mb_frame.grid(row = 0, column = 0)
update_all = Button(mb_frame, text = "Update All")
update_all.grid(row = 0, column = 0)
remove_all = Button(mb_frame, text = "Remove All")
remove_all.grid(row = 0, column = 1)
reset_default = Button(mb_frame, text = "Reset to Default")
reset_default.grid(row = 0, column = 2)

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

main_window.mainloop()