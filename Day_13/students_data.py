import json
class student:
  def __init__(self,name,age,marks):
    self.name=name
    self.age=age
    self.marks=marks
  def to_dict(self):#object-->dictionary
    return{
      "name":self.name,
      "age":self.age,
      "marks":self.marks
    }
s1=student("Pavan",21,90)#objects created
s2=student("Ravi",22,85)

students=[s1.to_dict(),s2.to_dict()] #objects to list of dicts

with open("students.json","w")as file:
  json.dump(students,file,indent=4)#converts python data to json format

#Read
with open("students.json","r")as file:
  data=json.load(file)#converts json>python
#convert back to objects from dictionary
students=[]
for item in data:
  students.append(student(item["name"],item["age"],item["marks"]))
#display
for s in students:
  print(s.name,s.age,s.marks)