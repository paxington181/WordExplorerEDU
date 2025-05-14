import tkinter as tk
from tkinter import *

def main():
    word_list = []
    definition_list = []

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

#Reads through the list of words and definitions and gives ordered boxes that are easier for users that are less comfortable with computers to manipulate the word list.

    print(word_list)
    print(len(word_list))   
    print(definition_list)
    print(len(definition_list))

main()
