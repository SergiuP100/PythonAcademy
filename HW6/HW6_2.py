#Use the input function to read a list of names from console. The names should be separated by a comma.
#
#Ex: Marius, Ion, Vasile
#
#Using the string .split() method, you generate a list form the string, call the list list_of_names.
#
#For each name in the list_of_names, ask the user to input a grade, and store it in the list_of_marks.
#
#Note: You will notice that both lists should have the same length, and the indices for marks and names correspond.
#
#Afterward do the following:
#
#Display the full list of names, and their grades in the following format: "Marius got grade: 10"
#Calculate the sum of all grades
#Calculate the average grade.
#Complete the ___ with the necessary code.

names = input("Please type a list of names separated by comma :  ")
list_of_names = names.split(',')

list_of_marks = []

for name in list_of_names:
    themark = input(f"Please type the correct grade for {name} = ")
    list_of_marks.append(themark)
print("Lista de note : ", list_of_marks)

marks_sum = 0
for mark in list_of_marks:
    marks_sum += int(mark)

print(f"\nSuma notelor: {marks_sum}")
print(f"Media notelor: {marks_sum / len(list_of_marks)}\n")

for i in list_of_names:
    print(f"{i} got grade: {list_of_marks[list_of_names.index(i)]}")
