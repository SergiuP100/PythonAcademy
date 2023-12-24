from urllib.request import urlopen

# extracting data
link = 'https://www.gutenberg.org/cache/epub/1513/pg1513.txt'
response = urlopen(link)
text = response.read()

# converting to string
all_text = str(text, encoding='utf-8')

# removing punctuation
punct = ",.:[]#*''“;_!?-()$•’/\\‘—"
for i in all_text:
    if i in punct:
        all_text = all_text.replace(i, " ")
all_text = all_text.split()
a = set(all_text)
list_words = list(a)

# creating zero's list for counting
list_times = [0]
for i in range(1, len(list_words)):
    list_times.append(0)

# counting the freq of words
for i in list_words:
    for x in all_text:
        if x == i:
            list_times[list_words.index(i)] += 1
#    print(list_times[list_words.index(i)], end = " ")
print("Total number of words in the text is : ", len(list_words))

# creating 2 lists of 50 most used and 50 least used words
most_used = []
most_used_freq = []
i = 0
while i < 50:
    place = list_times.index(max(list_times))
    most_used.append(list_words[place])
    most_used_freq.append(list_times[place])
    del list_words[place]
    del list_times[place]
    i += 1
print("List of the 50 most used words           : ", most_used)
print("Frequency list of the 50 most used words : ", most_used_freq)

least_used = []
least_used_freq = []
i = 0
while i < 50:
    place = list_times.index(min(list_times))
    least_used.append(list_words[place])
    least_used_freq.append(list_times[place])
    del list_words[place]
    del list_times[place]
    i += 1
print("List of the 50 least used words          : ", least_used)
print("Frequency list of the 50 least used words: ", least_used_freq)

