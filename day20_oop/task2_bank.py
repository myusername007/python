class BankAccount:
    def __init__(self, owner, balance =0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Deposit can`t be negative or zero")
    
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew: {amount}")
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.balance
    
    def __repr__(self):
        return f"Owner: {self.owner}, Balance: {self.balance}"
    
account = BankAccount("Roma", 200)
print(account)
account.deposit(150)
print(account)
account.withdraw(100)
print(account)
account.withdraw(500)
print(account)
account.deposit(-50)
print(account)
print(f"Current Balance: {account.get_balance()}")


    
