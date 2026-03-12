students = {}

while True:
    print("\n---- Dictionary Operations ----")
    print("1. Add Student")
    print("2. Update Marks")
    print("3. Delete Student")
    print("4. Search Student")
    print("5. Display Students")
    print("6. Show Keys")
    print("7. Show Values")
    print("8. Show Items")
    print("9. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        name = input("Enter student name: ")
        marks = int(input("Enter marks: "))
        students[name] = marks
        print("Student added")

    elif choice == 2:
        name = input("Enter student name: ")
        if name in students:
            marks = int(input("Enter new marks: "))
            students[name] = marks
            print("Marks updated")
        else:
            print("Student not found")

    elif choice == 3:
        name = input("Enter student name: ")
        if name in students:
            del students[name]
            print("Student deleted")
        else:
            print("Student not found")

    elif choice == 4:
        name = input("Enter student name: ")
        print(students.get(name, "Student not found"))

    elif choice == 5:
        print("Students:", students)

    elif choice == 6:
        print("Keys:", students.keys())

    elif choice == 7:
        print("Values:", students.values())

    elif choice == 8:
        print("Items:", students.items())

    elif choice == 9:
        print("Program ended")
        break

    else:
        print("Invalid choice")