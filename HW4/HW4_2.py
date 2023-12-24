string = input("Write a String of characters : ")
letters = 0
vowels = 0
consonants = 0
for i in string:
    if i.isalpha() == True:
        letters += 1
    if(i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U'):
        vowels += 1
    if i not in "aeiouAEIOU " and i.isalpha():
        consonants += 1
print('No of letters:', letters)
print('No of vowels:', vowels)
print('No of consonants:', consonants)
