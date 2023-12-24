pass1 = input("Please type the new password : ")
if pass1.islower() or pass1.isupper() or pass1.isnumeric() or len(pass1) < 8:
    print("Password is weak!")
low = upp = num = 0
for i in pass1:
    if i.islower():
        low += 1
    if i.isupper():
        upp += 1
    if i.isnumeric():
        num += 1
if ((low and upp and not num) or (low and num and not upp) or (upp and num and not low)) and len(pass1) > 8:
    print("Password is good!")
if low and upp and num and len(pass1) > 8:
    print("Password is strong!")

