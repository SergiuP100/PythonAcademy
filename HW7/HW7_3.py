# Time Converter
# Write a program that takes time from user input in the following format: "11:20 PM" or "02:00 AM".
# And converts it to 24-Hour format. "23:20" or "02:00"
#
# Note: write all the logic yourself, do not rely on built-in modules.

user_time = input("Please type the time in the following format - \"hh:mm AM/PM\" (hh as hour, mm as minutes : ")
if user_time[-2:] == 'PM':
    print(f"24-Hour format is :  {int(user_time[:2]) + 12}:{user_time[3:5]}")
elif user_time[-2:] == 'AM':
    print(f"24-Hour format is :  {(user_time[:2])}:{user_time[3:5]}")
