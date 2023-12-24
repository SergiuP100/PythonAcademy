# From user input create three separate lists
# that represent the names of participants present at three different events.
#
# Using set operations (after you transform the lists to sets), find out the following info.
#
# Which of the participants have participated at all events.
# Which of the participants have only participated at the first event.
# Which of the participants have only participated at the second event.
# Which of the participants from the 1st event participated also at the 3rd event ?

text1 = input("Please type the names of participants from the first event, separated by space : ")
list1 = set(text1.split())
text2 = input("Please type the names of participants from the second event, separated by space : ")
list2 = set(text2.split())
text3 = input("Please type the names of participants from the third event, separated by space : ")
list3 = set(text3.split())

rez1 = list1.intersection(list2.intersection(list3))
if len(rez1):
    print("Participants who have participated at all events : ", rez1)
else:
    print("No participants been on all events !")

rez2 = list1.difference(list2)
rez2_1 = rez2.difference(list3)
if len(rez2_1):
    print("Participants who have only participated at the first event : ", rez2_1)
else:
    print("No participants been only at the first event !")

rez3 = list2.difference(list1)
rez3_1 = rez3.difference(list3)
if len(rez3_1):
    print("Participants who have only participated at the second event : ", rez3_1)
else:
    print("No participants been only at the second event !")

rez4 = list1.intersection(list3)
if len(rez4):
    print("Participants from the 1st event who participated also at the 3rd event  : ", rez4)
else:
    print("No participants from first event been at the third event !")

