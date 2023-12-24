temp1 = float(input("Please type the Celsius temperature "))
if temp1 <= -10:
    print("It feels: Extremely freezing")
elif -10 < temp1 <= 0:
    print("It feels: Freezing")
elif 0 < temp1 <= 10:
    print("It feels: Cold")
elif 10 < temp1 <= 20:
    print("It feels: Comfortable")
elif 20 < temp1 <= 30:
    print("It feels: Warm")
elif 30 < temp1 <= 40:
    print("It feels: Extremely Warm")
elif temp1 > 40:
    print("It feels: Apocalypse")
