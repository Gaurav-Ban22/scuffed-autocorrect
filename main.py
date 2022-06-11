from difflib import SequenceMatcher

ask = input("Write a word and don't worry about correct spelling: ")

file = open("words_alpha.txt", "r")
best = 0
word = ""
for x in file:
    r = SequenceMatcher(None, ask, x)
    rat = r.ratio()
    if rat > best:
        best = rat
        word = x

print(word)
    