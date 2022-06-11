from difflib import SequenceMatcher

ask = input("Write a statement and don't worry about correct spelling: ")
lis = ask.split()
print(lis)

final = ""

for y in lis:
    word = ""
    best = 0
    with open("words_alpha.txt", "r") as file:
        for line in file:
            r = SequenceMatcher(None, y, line)
            rat = r.ratio()
            if rat >= best:
                best = rat
                word = line
                #print(word)
    final += word 
    print(final, end = "")
file.close()
print("Did you mean to say\n" + final)
    


    