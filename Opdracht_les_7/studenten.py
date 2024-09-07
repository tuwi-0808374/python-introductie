from students_classrooms import students_per_classroom

# print(type(students_per_classroom))
# print(type(students_per_classroom["SWDVT-1A"]))

def is_student_excellent(student):
    excellent = True
    for result in student['resultaten']:
        if student['resultaten'][result] == "uitmuntend":
            excellent = True
            break
        if student['resultaten'][result] == "voldoende" or student['resultaten'][result] == "onvoldoende":
            excellent = False
    return excellent

def get_most_excellent_classroom():
    classes = []
    for c_name in students_per_classroom:
        amount_students = 0
        amount_ex_students = 0
        for student in students_per_classroom[c_name]:
            amount_students += 1
            if is_student_excellent(student):
                amount_ex_students += 1
        classes.append({'klas': c_name, 'aantal_studenten':amount_students, 'aantal_ex_studenten':amount_ex_students})
    # print(classes)
    best_class = ("name", 0.0)
    for cl in classes:
        percentage = (cl['aantal_ex_studenten'] / cl['aantal_studenten']) * 100
        if percentage > best_class[1]:
            best_class = (cl['klas'], percentage)
        print(f"{cl['klas']}  {percentage}%")
    print(f"Beste klass is: {best_class[0]}")

for c_name in students_per_classroom:
    for student in students_per_classroom[c_name]:
        # print(student)
        # print(student['naam'])
        if is_student_excellent(student):
            print(f"Student: {student['naam']} is excellent")

get_most_excellent_classroom()