# Guessing Game
# Write a program that generates a random number between 1 and 100 and lets the user guess the number.
# The program should provide feedback ("higher" or "lower") until the user guesses the correct number.
# The program should also keep track of the number of guesses it takes for the user to guess correctly.
from random import randint

random_number = randint(1, 100)
number_guessed = 0
count = 0
while number_guessed != random_number:
    count += 1
    number_guessed = int(input(f"Guess Number : '{count}'. Please type the number : "))
    if number_guessed == random_number:
        print(f"\nIt took you  : '{count}' tries, to guess the random number : '{random_number}'")
    elif number_guessed < random_number:
        print("     You should try a higher number!")
    else:
        print("     You should try a lower number!")
