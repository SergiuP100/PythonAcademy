# Let the user enter a list of numbers separated by a comma as input. E.g 5,4,3,2,8,9,10,19.
#
# Calculate the following:
#
# the sum of all even
# the sum of all odd
# numbers in the list.
sum_even = sum_odd = total = 0
numbers_input = input("Please type a list of numbers separated by comma : ")
list_of_numbers = numbers_input.split(',')
for i in list_of_numbers:
    if not int(i) % 2:
        sum_even += int(i)
    else:
        sum_odd += int(i)
    total += int(i)
print("The sum of all even numbers = ", sum_even)
print("The sum of all odd numbers = ", sum_odd)
print("The sum of all even numbers = ", total)
