# Write a program that takes a sentence as input.
# The program should count the letters of each word that start with the letters 'A' and 'T', (case insensitive),
# and print those words and collect the sum of the lengths of those words.
# If the word starts with any other letter, it must print "Skipping word" and continue to the next one.
# The solution must incorporate the continue statement.

text = input("Please type in the sentence : ")
text = text.replace(',', '')
text = text.replace('.', '')
word_list = text.split()
sum_length = 0
for i in word_list:
    if i[0].upper() != 'A' and i[0].upper() != 'T':
        print("Skipping word")
        continue
    else:
        sum_length += len(i)
        print(f"Word: {i} - has {len(i)} letters")
print(f"The sum of the lengths of those words is = {sum_length} letters")
