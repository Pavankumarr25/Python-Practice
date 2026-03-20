class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def display(self):
        print("\nStudent Details")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Marks:", self.marks)


name = input("Enter name: ")
age = int(input("Enter age: "))
marks = float(input("Enter marks: "))

s1 = Student(name, age, marks)
s1.display()