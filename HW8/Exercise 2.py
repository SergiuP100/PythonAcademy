# User Input Sum: Take input from the user until they enter 0,
# then print the sum of all entered numbers using a while loop.

num = -1
sum_num = 0
while num != 0:
    num = float(input("Enter a number please : "))
    if num != 0:
        sum_num += num
print("The sum of all entered numbers is : ", sum_num)
