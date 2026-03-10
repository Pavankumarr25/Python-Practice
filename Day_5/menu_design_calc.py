while True:
  print("1.Addition")
  print("2.Substraction")
  print("3.Multiplication")
  print("4.Division")
  print("5.Modulus")
  print("6.Power")
  print("7.Exit")


  choice=int(input("Enter a choice: "))

  if choice==1:
    a=float(input("Enter 1st number"))
    b=float(input("Enter 2nd number"))
    print("Result",a+b)
  elif choice==2:
    a=float(input("Enter 1st number"))
    b=float(input("Enter 2nd number"))
    print("Result",a-b)
  elif choice==3:
    a=float(input("Enter 1st number"))
    if b!=0:
         print("Result",a*b)
    else:
        print("Cannot divide by 0")
  elif choice==4:
      a=float(input("Enter 1st number"))
      b=float(input("Enter 2nd number"))
      print("Result",a/b)
  elif choice==5:
      a=float(input("Enter 1st number"))
      b=float(input("Enter 2nd number"))
      print("Result",a%b)
  elif choice==6:
      a=float(input("Enter 1st number"))
      b=float(input("Enter 2nd number"))
      print("Result",a**b)
  elif choice == 7:
      print("Exiting Calculator...")
      break
  else:
     print("choose the correct option")



