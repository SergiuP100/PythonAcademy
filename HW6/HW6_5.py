# More data storage
# Create two lists: student_1 and student_2.
#
# Both of the lists should then store the grade and the name of the student it represents.
#
# Calculate which student has the highest grade, and display that information in a print statement.
#
# The information for the print and calculation should be used from the lists and not from other sources.

student_1 = []
student_2 = []
student_1 = [input("Please type the name of the first student : "), input("Please type his/her grade : ")]
student_2 = [input("Please type the name of the second student : "), input("Please type his/her grade : ")]
if int(student_1[1]) > int(student_2[1]):
    print(f"{student_1[0]} has the highest grade = {student_1[1]}")
elif int(student_2[1]) > int(student_1[1]):
    print(f"{student_2[0]} has the highest grade = {student_2[1]}")
else:
    print(f"Both students have the same grade = {student_2[1]}")
