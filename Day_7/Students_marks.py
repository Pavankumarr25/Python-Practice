marks = []

for i in range(5):
    m = int(input("Enter marks: "))
    marks.append(m)

total = sum(marks)
average = total / len(marks)

print("Marks:", marks)
print("Total:", total)
print("Average:", average)