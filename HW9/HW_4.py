# Write a program that generates random numbers between 1 and 10 using a while loop.
# The program should continue generating numbers until it generates a number greater than 8.
# Once the number is greater than 8, the program should terminate the loop using the break statement.
from random import randrange

i = True
print("Randomizing started!")
while i:
    random_number = randrange(1, 10)
    print("Random number = ", random_number)
    if random_number > 8:
        break
