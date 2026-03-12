set1=set()
while True:
  print("\n-------Set Operations--------------")
  print("1. Add Elements")
  print("2. Remove Elements")
  print("3. Display Set")
  print("4. Union")
  print("5. Intersecton")
  print("6. Difference")
  print("Exit")

  choice=int(input("Enter choice:"))

  if choice==1:
    element=int(input("Enter element"))
    set1.add(element)
    print("element added")
  elif choice== 2:
    element=int(input("Enter element to remove"))
    if element in set1:
      set1.remove(element)
      print("Element removed")
    else:
      print("Element not found")
  elif choice == 3:
    print("set:",set1)
  elif choice== 4:
    set2={4,5,6}
    print ("Union:",set1 | set2)
  elif choice== 5:
    set2={4,5,6}
    print("Intersection:",set1 & set2)
  elif choice==6:
    set2={4,5,6}
    print("Difference:",set1 - set2)
  elif choice== 7:
    print("Program ended")
    break
  else:
    print("Invalid choice")
