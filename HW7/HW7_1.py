# BMI Calculator
# Write a program that takes a person's weight (in kilograms) and height (in meters, e.g. 1.75)
# as input and calculates their Body Mass Index (BMI). Then classify the BMI into the following categories:
#
# Underweight (BMI < 18.5) Normal weight (BMI between 18.5 and 24.9) Overweight (BMI between 25 and 29.9)
# Obesity (BMI 30 or greater)
#
# In order to calculate BMI use the steps below:
#
# Take the weight in KG and height in M.
# The BMI formula is BMI = Weight / Height * Height.

weight = float(input("Please type the person weight in kg : "))
height = float(input("Please type the person height in meters : "))
bmi = weight / (height * height)
if bmi < 18.5:
    print("Person is Underweight!")
elif 18.5 <= bmi <= 24.9:
    print("Person has Normal Weight!")
elif 25 <= bmi <= 29.9:
    print("Person is Overweight!")
elif bmi >= 30:
    print("Person has Obesity")
