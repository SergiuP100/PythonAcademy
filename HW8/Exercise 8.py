# Factorial with Range: Calculate the factorial of a number using a for loop and the range function.
number_fact = int(input("Please type the number to calculate the factorial : "))
factorial = 1
if number_fact == 0:
    print("The factorial for '0' is '1'")
else:
    for i in range(1, number_fact+1):
        factorial *= i
        print(f"The factorial for '{number_fact}' is '{factorial}'")
