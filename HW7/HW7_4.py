# Anagram Detector
# Write a program that takes 2 separate words as input. The program should check if the two words are anagrams.
#
# Anagrams are words that can have their letters re-arranged to form another word.
#
# Examples:
#
# dormitory → dirty room
# debit card → bad credit
# angered → enraged
# funeral → real fun
print("Hello, we are going to check if 2 inputs are anagrams!  No punctuation allowed.")
word1 = input("Please type the first part : ")
word2 = input("Please type the second part : ")
word2_1 = word2.replace(" ", "")
for i in word1:
    count = 0
    for x in word2_1:
        if i == x:
            word2_1 = word2_1.replace(x, "")
if word2_1 == '':
    print("Anagrams detected!")
else:
    print("After verifying, anagrams not found!")
