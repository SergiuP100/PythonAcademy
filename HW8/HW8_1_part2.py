# Write a program that uses a while loop to generate the Fibonacci sequence up to a given number of terms.
# The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones.
# The sequence starts with 0 and 1.
# Solve this exercise using both for and while
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233

fib_len = int(input("Please introduce the length you want to be generated for Fibonacci sequence : "))
i = 0
y = 1
print(0, 1, end =' ')
for a in range(1, fib_len-1):
    x = i + y
    print(x, end = ' ')
    i = y
    y = x
