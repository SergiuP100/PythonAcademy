# Write a program that takes a list of numbers as input.
# The program should calculate the product of all the numbers in the list.
# However, if the product exceeds 100, the program should stop calculating
# and print a message indicating that the product is too large.
# Use a for loop and the break statement to terminate the loop when necessary.

text = input("Please type a list of numbers separated by comma :  ")
nr_list = text.split(',')
nr_product = 1
for i in nr_list:
    if nr_product > 100:
        print("The product is too large! ")
        break
    nr_product *= int(i)
print(f"The product for numbers in the list is:  {nr_product}")

nr_product = 1
count = 0
while count < len(nr_list):
    nr_product *= int(nr_list[count])
    if nr_product > 100:
        print("The product is too large! ")
        break
    elif count == len(nr_list)-1:
        print(f"The product for numbers in the list is:  {nr_product}")
    count += 1
