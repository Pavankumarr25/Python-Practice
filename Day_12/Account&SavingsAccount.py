# Parent Class
class Account:
    def __init__(self, acc_number, holder_name, balance):
        self.acc_number = acc_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}")
        print(f"New Balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn: {amount}")
            print(f"Remaining Balance: {self.balance}")
        else:
            print("Insufficient Balance!")

    def display(self):
        print("\n--- Account Details ---")
        print("Account No:", self.acc_number)
        print("Name:", self.holder_name)
        print("Balance:", self.balance)


# Child Class
class SavingsAccount(Account):
    def __init__(self, acc_number, holder_name, balance, interest_rate):
        super().__init__(acc_number, holder_name, balance)  # calling parent constructor
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = (self.balance * self.interest_rate) / 100
        self.balance += interest
        print(f"Interest Added: {interest}")
        print(f"Updated Balance: {self.balance}")


# Using the classes
acc1 = SavingsAccount(101, "Pavan", 10000, 5)

acc1.display()
acc1.deposit(2000)
acc1.withdraw(3000)
acc1.add_interest()
acc1.display()