
student_dict = {}
total_student = int(input("Enter the total number of student: "))
student = 0
while student < total_student:
    name = input('Enter the student name: ')
    attendance = int(input("Enter the attendance percentage"))
    student_dict[name] = attendance
    student = student + 1

print(student_dict)


# function to return key for any value
def get_key(key1):
    for key, val in student_dict.items():
        if key1 == key:
            return val


for student in student_dict.keys():
    value = get_key(student)
    if value >= 95:
        print(student, " got ", 5, ' marks in attendance')
    elif value in range(90, 95):
        print(student, " got ", 4, ' marks in attendance')
    elif value in range(85, 90):
        print(student, " got ", 3, ' marks in attendance')
    elif value in range(80, 85):
        print(student, " got ", 2, ' marks in attendance')
    else:
        print(student, " got ", 1, ' marks in attendance,\n Need to get permission!')
