print("1.Add")
print("2.Substract")
print("3.Divide")
print("4.Multiply")
print("5.Modulus")
print("6.Power")
print("7.Exit")

choice=int(input("Enter your choice(1-4) "))

a=float(input("Enter first number"))
b=float(input("Enter second number"))

if choice==1:
  print("Result",a+b)
elif choice==2:
  print("Result",a-b)
elif choice==3:
  if b!=0:
    print("Result",a/b)
  else:
    print("Cannot divide by 0")
elif choice==4:
  print("Result",a*b)
elif choice==5:
  print("Result",a%b)
elif choice==6:
  print("Result",a**b)
else:
  print("choose the correct option")
