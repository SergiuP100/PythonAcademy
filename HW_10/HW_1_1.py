from urllib.request import urlopen

# extracting data
link = 'https://www.gutenberg.org/cache/epub/1513/pg1513.txt'
response = urlopen(link)
text = response.read()

# converting to string
all_text = str(text, encoding='utf-8')

# removing punctuation
punct = ",.:[]#*'';_!?-()$•’/\\"
response = " "
for i in all_text:
    if i in punct:
        all_text = all_text.replace(i, "")
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
# list_words = ['word1', 'word2', 'word3', 'word4', 'word5', 'word6', 'word7']
# list_times = [   9,       7,       5,       4,       5,       6,       7]
# index =          0        1        2        3        4        5        6
most_used = []
i = 0
while i < 50:
    place = list_times.index(max(list_times))
    most_used.append(list_words[place])
    del list_words[place]
    del list_words[place]
    i += 1
print("List of the 50 most used words : ", most_used)

least_used = []
i = 0
while i < 50:
    place = list_times.index(min(list_times))
    least_used.append(list_words[place])
    del list_words[place]
    del list_words[place]
    i += 1
print("List of the 50 least used words : ", least_used)

# The program would have to tell the user the following:
# Total number of words in the text
# Top 50 most used words
# Top 50 least used words

# List of the 50 most used words :  ['the', 'knocks', 'account', 'lead', 'sound', 'defence', 'nose', 'drivelling', 'illdivining', 'banishd', 'comest', 'production', 'match', 'why', 'Chorus', 'words', 'thrown', 'didst', 'Montagues', 'loving', 'dumps', 'armed', 'hard', 'gnat', 'hall', 'Servants', 'tall', 'unmannd', 'reuse', 'dreamers', 'highway', 'deathmarkd', 'touching', 'joind', 'Retires', 'subscribe', 'commend', 'advancd', 'Brags', 'braggart', 'Immediately', 'Mercutio', 'breathe', 'cause', 'Throws', 'true', '‘Ah', 'looking', 'how', 'thrice']
# List of the 50 least used words :  ['eats', 'teat', 'Oercoverd', 'Could', 'trouble', 'post', 'Whats', 'paper', 'fought', 'Live', 'journey', 'mousehunt', 'ensuring', 'apprehend', 'pray', 'infringement', 'unfurnishd', 'seemst', 'starvd', 'virtues', 'stick', 'NO', 'relations', 'maidenwidowed', 'been', 'MUSICIAN', 'soar', 'break', 'Weeping', 'Draw', 'Fie', 'dissemblers', 'staff', 'Against', 'yourself', 'MERCHANTABILITY', 'dire', 'cursed', 'binary', 'dust', 'begone', 'hath', '“It', 'unprotected', 'fish', 'Michael', 'men', 'mean', 'pestilence', 'mother']
