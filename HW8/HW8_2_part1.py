# Prime check
# Write a program that will check that a given number (from input) is prime or not.
# A number is prime if it can only be divided by 1 and itself. You can check the divisors using the modulo function.
# Number 5 is prime because: 5 % 1 == 0 5 % 2 == 1 5 % 3 == 2 5 % 4 == 1 5 % 5 == 0
# Every number other than 1 and 5 is not a divisor.
# Implement this exercise using both For and While loops

counter = 0
number = int(input("Please type a number to check for prime : "))
for i in range(2, number):
    if number % i == 0:
        counter += 1
if counter == 0:
    print(f"The number is '{number}' is prime!")
else:
    print(f"The number is '{number}' is not prime!")
