#
# List Sum: Calculate and print the sum of elements in a list using a for loop.

valori = input("Please type the elements of the list, separated by comma :  ")
list_of_numbers = valori.split(',')
sum = 0
for i in list_of_numbers:
    sum += int(i)
print("The sum of elements is = ", sum)