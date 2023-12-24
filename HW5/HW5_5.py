min_points = int(input("Please type the minimum points to pass the test: "))
student_name = input("Please type the student name : ")
student_points = int(input(f"Please type {student_name} amount of points : "))
if student_points >= min_points:
    print(f"Student {student_name} passed the test!")
else:
    print(f"Student {student_name} failed the test!")
