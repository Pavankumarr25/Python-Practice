def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def modulus(a, b):
    return a % b
while True:

    print("\n----- Calculator Menu -----")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Modulus")
    print("6. Exit")

    choice = int(input("Enter your choice: "))
    if choice == 6:
        print("Exiting calculator...")
        break

    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    if choice == 1:
        print("Result:", add(a, b))

    elif choice == 2:
        print("Result:", subtract(a, b))

    elif choice == 3:
        print("Result:", multiply(a, b))

    elif choice == 4:
        print("Result:", divide(a, b))

    elif choice == 5:
        print("Result:", modulus(a, b))

    else:
        print("Invalid choice")

    