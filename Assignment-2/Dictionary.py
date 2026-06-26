def add_student(students):
    name = input("Enter student name: ")
    grade = input("Enter student grade: ")
    students[name] = grade
def update_student(students):
    name = input("Enter student name: ")
    if name in students:
        students[name] = input("Enter new grade: ")
    else:
        print("Student not found.")
def print_students(students):
    for name, grade in students.items():
        print(f"{name}: {grade}")