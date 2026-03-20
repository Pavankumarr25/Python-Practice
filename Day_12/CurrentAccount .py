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
        else:
            print("Insufficient Balance!")

    def display(self):
        print("\n--- Account Details ---")
        print("Account No:", self.acc_number)
        print("Name:", self.holder_name)
        print("Balance:", self.balance)


# Child Class - Current Account
class CurrentAccount(Account):
    def __init__(self, acc_number, holder_name, balance, overdraft_limit):
        super().__init__(acc_number, holder_name, balance)
        self.overdraft_limit = overdraft_limit

    # Overriding withdraw method
    def withdraw(self, amount):
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            print(f"Withdrawn: {amount}")
            print(f"Balance (can be negative): {self.balance}")
        else:
            print("Overdraft limit exceeded!")

    def display(self):
        super().display()
        print("Overdraft Limit:", self.overdraft_limit)


# Using the class
acc2 = CurrentAccount(202, "Pavan", 5000, 3000)

acc2.display()
acc2.withdraw(7000)   # Allowed (5000 + 3000)
acc2.withdraw(2000)   # Exceeds limit
acc2.deposit(4000)
acc2.display()