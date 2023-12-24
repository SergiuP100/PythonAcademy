#
# Nested Loop: Print a pattern using nested for loops. Output:
#
# 1
# 1 2
# 1 2 3

end_number = int(input("Please introduce a number between 3 and 5 : "))
for i in range(1, end_number-1):
    if i == 1:
        print(i)
    for x in range(i+1, end_number):
        if x == 2:
            print(i, x)
        for y in range(i+2, end_number+1):
            if x - i == 1 and y - x == 1 and not i - 1:
                print(i, x, y)
            elif x - i == 1 and y - x == 1 and not i - 2:
                print(i-1, i, x, y)
            elif x - i == 1 and y - x == 1 and not i - 3:
                print(i-2, i-1, i, x, y)
