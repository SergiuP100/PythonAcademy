text = input("Write a text :  \n")
y = -1
palindrome = 1
for i in text:
        if i != text[y]:
            palindrome = 0
            break
        y = y - 1
if palindrome == 1:
    print('Text is Palindrome')
else:
    print("Text is not Palindrome")