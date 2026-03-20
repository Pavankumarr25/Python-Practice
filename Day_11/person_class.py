class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def profile(self):
        print("Person Profile:")
        print("Name:", self.name)
        print("Age:", self.age)
        print("City:", self.city)


# Create object
p1 = Person("Pavan", 21, "Hyderabad")

# Call method
p1.profile()