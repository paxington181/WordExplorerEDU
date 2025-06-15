import json

with open("default_wordlist.json", "r") as file:
    default_wordlist = json.load(file)

print(default_wordlist)
