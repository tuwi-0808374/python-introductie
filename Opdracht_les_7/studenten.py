from students_classrooms import students_per_classroom

# print(type(students_per_classroom))
# print(type(students_per_classroom["SWDVT-1A"]))


def excellent_students_from_classroom(students):
    excellent = True
    excellent_students = []
    for result in student['resultaten']:
        if student['resultaten'][result] == "uitmuntend":
            excellent = True
            break
        if student['resultaten'][result] == "voldoende" or student['resultaten'][result] == "onvoldoende":
            excellent = False
    if excellent:
        excellent_students.append(student)
    return excellent_students

for c_name in students_per_classroom:
    for student in students_per_classroom[c_name]:
        # print(student)
        # print(student['naam'])
        for ex_stu in excellent_students_from_classroom(student):
            print(f"Student: {student['naam']} is excellent")

def get_most_excellent_classroom():
    pass

# def get_excellent_students(students):
#     excellent_students = []
#     print(excellent_students)
#
# get_excellent_students(students)
