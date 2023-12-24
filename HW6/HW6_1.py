#Having the list below.
#
#Add 4, 5, 6 to it and print out the list.
#
#my_list = [1, 2, 3]
#Copy
#Use at least 2 ways of adding elements.
#
#Afterward, remove only the value 4 from the list.
#
#And after that remove the last item from the list

my_list = [1, 2, 3]
my_list.append(4)
my_list.append(5)
my_list.append(6)
print(my_list)

my_list = [1, 2, 3]
my_list2 = [4, 5, 6]
my_list = my_list + my_list2
print(my_list)

my_list = [1, 2, 3]
my_list2 = [4, 5, 6]
my_list.extend(my_list2)
print(my_list)

my_list.remove(4)
print(my_list)

my_list.pop()
print(my_list)
