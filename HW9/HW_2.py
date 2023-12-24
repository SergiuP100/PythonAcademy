# Write a list comprehension that generates a list of the lengths of the words in a given sentence.
# For example, if the sentence is "Hello world, how are you?", the list comprehension should produce [5, 5, 3, 3, 4].
#
# Write a list comprehension that generates a list of the uppercase letters in a given string.
# For example, if the string is "Hello World", the list comprehension should produce ['H', 'W'].
#
# Write a list comprehension that generates a list of the first letter of each word in a given sentence.
# For example, if the sentence is "Python is awesome", the list comprehension should produce ['P', 'i', 'a'].

text = input("Please type in the sentence : ")
text = text.replace(',', '')
word_list = text.split()
list_length = [len(word) for word in word_list]
print(list_length)

upp_list = [el for el in text if el.isupper()]
print(upp_list)

first_letter_list = [el[0] for el in word_list]
print(first_letter_list)