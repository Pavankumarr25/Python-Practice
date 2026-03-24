import json

FILE = "students.json"

class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def to_dict(self):
        return {
            "name": self.name,
            "age": self.age,
            "marks": self.marks
        }

# Load existing data
def load_students():
    try:
        with open(FILE, "r") as file:
            return json.load(file)
    except:
        return []

# Save data
def save_students(data):
    with open(FILE, "w") as file:
        json.dump(data, file, indent=4)

# Add multiple students
def add_students():
    data = load_students()

    n = int(input("How many students to add: "))

    for _ in range(n):
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        marks = int(input("Enter marks: "))

        student = Student(name, age, marks)
        data.append(student.to_dict())

    save_students(data)
    print("Students saved successfully!")

# View students
def view_students():
    data = load_students()

    if not data:
        print("No students found")
        return

    for s in data:
        print(f"{s['name']} - Age: {s['age']} - Marks: {s['marks']}")

# Menu
while True:
    print("\n1.Add Students\n2.View Students\n3.Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        add_students()
    elif choice == "2":
        view_students()
    elif choice == "3":
        break
    else:
        print("Invalid choice")