# Password Checker: Ask the user to enter a password,
# and keep prompting until they enter the correct password ('secret') using a while loop.

passw = ''
while passw != 'secret':
    passw = input("Enter the correct password : ")
print("The password entered is correct!")
