from option import opt
from Dictionary import add_student, update_student, print_students

students = {}
while True:
    choice = opt()
    if choice == '1':
        add_student(students)
    elif choice == '2':
        update_student(students)
    elif choice == '3':
        print_students(students)
    elif choice == '4':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")