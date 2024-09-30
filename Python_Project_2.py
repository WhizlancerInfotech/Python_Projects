class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} deposited. New balance is {self.balance}.")
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"{amount} withdrawn. New balance is {self.balance}.")
    
# Create a bank account
account = BankAccount("Alice", 1000)

# Perform some transactions
account.deposit(500)
account.withdraw(300)
account.withdraw(1500)
