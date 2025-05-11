def main():
    word_list = []
    definition_list = []
    
    with open("wordlist.txt") as file:
        unmodified_wordlist = file.read().splitlines()
        for line in unmodified_wordlist:
            if line.startswith("#"):
                unmodified_wordlist.remove(line)
            elif line.startswith("w."):
                word_list.append(line[2:])
            elif line.startswith("d."):
                definition_list.append(line[2:])
    
    print(word_list)
    print(definition_list)
main()
