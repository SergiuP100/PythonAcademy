# Create a Python function to generate the Fibonacci sequence up to a specified number of terms.
# The Fibonacci sequence starts with 0 and 1, and each subsequent term is the sum of the two preceding ones.
#    endpoint = int(input("Please introduce the length you want to be generated for Fibonacci sequence : "))
#    nr_lista = [0, 1]
#    print(nr_lista)
#    for i in range(2, endpoint+1):
#        nr_lista.append(nr_lista[i-1]+nr_lista[i-2])
#    print(nr_lista)

# Write a program that uses a while loop to generate the Fibonacci sequence up to a given number of terms.
# The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones.
# The sequence starts with 0 and 1.
# Solve this exercise using both for and while
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233

fib_len = int(input("Please introduce the length you want to be generated for Fibonacci sequence : "))
i = 0
y = 1
parser = 2
print(0, 1, end =' ')
while parser <= fib_len:
    x = i + y
    print(x, end = ' ')
    parser += 1
    i = y
    y = x

fib_len = int(input("Please introduce the length you want to be generated for Fibonacci sequence : "))
i = 0
y = 1
print(0, 1, end =' ')
for a in range(1, fib_len+1):
    x = i + y
    print(x, end = ' ')
    i = y
    y = x
-------------------------------------------------

fib_len = int(input("Please introduce the length you want to be generated for Fibonacci sequence : "))
i = 0
y = 1
parser = 2
print(0, 1, end =' ')
while parser <= fib_len:
    x = i + y
    print(x, end = ' ')
    parser += 1
    i = y
    y = x