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
if ((low >= 1 and upp >= 1 and num == 0) or (low >= 1 and num >= 1 and upp == 0)
    or (upp >= 1 and num >= 1 and low == 0)) and len(pass1) > 8:
    print("Password is good!")
if low != 0 and upp != 0 and num != 0 and len(pass1) > 8:
    print("Password is strong!")

