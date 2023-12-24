import none

string1 = input("Please type a text : ")
if len(string1) <= 1:
    print("The text length is 1 or less!")
    exit()
character = input("Please type a character :  ")
if len(character) != 1:
    print("One character been expected. Goodbye")
    exit()
pos = 0
for i in string1:
    if i == character:
        print(f"The first found \"{character}\" character is on position : {string1.index(i)} in the text : {string1}")
        pos += 1
        exit()
if pos == 0:
    print("Character was not found in the text!")


