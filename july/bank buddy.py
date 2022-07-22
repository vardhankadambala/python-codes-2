class bank:
    def __init__(self):
        self.balance=0
        print("Hello !!! Welcome to the bank buddy")

    def __init__(self):
        self.balance1=0
        print("Hello !!! Welcome to the bank buddy")

    def deposit(self):
        amount = float(input("Enter the amout to be transfered"))
        self.balance += amount
        print("Amount Deposited",amount)

    def withdraw(self):
        amount = float(input("Enter the amout to be transfered"))
        self.balance -= amount

    def transfer(self):
        amount = float(input("Enter the amout to be transfered"))
        self.balance -= amount
        self.balance1 += amount
        print("amount transferred", amount)
        print("account balance is", self.balance)
