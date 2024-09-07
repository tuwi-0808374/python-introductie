from datetime import datetime

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

students = []
for c_name in students_per_classroom:
    for student in students_per_classroom[c_name]:
        students.append(student)

def get_excellent_students(list_of_students):
        for st in list_of_students:
            # print(student)
            # print(student['naam'])
            if is_student_excellent(st):
                print(f"\t- {st['naam']}")

def get_most_excellent_classroom(list_of_classrooms):
    classes = []
    best_class_name = ""
    best_class_percentage = 0
    best_class_ex_students = 0
    for c_name in list_of_classrooms:
        amount_students = 0
        amount_ex_students = 0
        for student in students_per_classroom[c_name]:
            amount_students += 1
            if is_student_excellent(student):
                amount_ex_students += 1
        classes.append({'klas': c_name, 'aantal_studenten':amount_students, 'aantal_ex_studenten':amount_ex_students})
    for cl in classes:
        percentage = (cl['aantal_ex_studenten'] / cl['aantal_studenten']) * 100
        if percentage > best_class_percentage:
            best_class_percentage = percentage
            best_class_name = cl['klas']
            best_class_ex_students = cl['aantal_ex_studenten']
    print(f"Klas met de meeste excellente studenten:\n \t -{best_class_name} met {best_class_ex_students} excellente studenten")

def get_score_score_student(student):
    score = 0
    results = student['resultaten'].values()
    for result in results:
        if result == "uitmunten":
            score += 4
        elif result == "goed":
            score += 3
        elif result == "voldoende":
            score += 2
        elif result == "onvoldoende":
            score += 0
    return score

def get_best_scoring_classroom(list_of_classrooms):
    class_name = ""
    class_score = 0
    for c_name in list_of_classrooms:
        score = 0
        for student in students_per_classroom[c_name]:
            score = get_score_score_student(student)
        if score > class_score:
            class_name = c_name
            class_score = score
    print(f"Klas met de hoogste scores gemiddeld:\n \t -{class_name} met {class_score} punten")

def get_failed_students(list_of_students, minimum_score = 4):
    for st in list_of_students:
        if get_score_score_student(st) < minimum_score:
            print(f"\t- {st['naam']}")
            for result in st['resultaten']:
                print(f"\t\t{result}: {st['resultaten'][result]}")


print(f"------ Rapport {datetime.today().strftime('%d-%m-%Y')} ------")
print("Excellente studenten: ")
get_excellent_students(students)
print()
get_most_excellent_classroom(students_per_classroom)
get_best_scoring_classroom(students_per_classroom)
get_failed_students(students, 3)
