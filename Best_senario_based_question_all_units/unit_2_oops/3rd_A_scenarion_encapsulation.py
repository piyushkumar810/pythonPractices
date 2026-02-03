'''
📝 Your Task
1️⃣ Create a class BankAccount
Attributes
account_holder → public
__balance → private (initial balance passed during object creation)

2️⃣ Methods (ALL REQUIRED)
show_balance()
→ prints current balance

deposit(amount)
→ adds amount to balance
→ amount must be positive

withdraw(amount)
→ subtracts amount from balance
→ withdrawal must not exceed balance

3️⃣ Rules (VERY IMPORTANT – EXAM CONDITIONS)

❌ Direct access like obj.__balance is NOT allowed
✔ Balance must be modified only via methods
✔ Use validation inside methods
✔ Follow encapsulation properly

🔍 Expected Usage
acc = BankAccount("Piyush", 5000)

acc.show_balance()
acc.deposit(2000)
acc.show_balance()
acc.withdraw(3000)
acc.show_balance()
acc.withdraw(6000)   # should show error

✅ Expected Output (logic-wise)
Current balance: 5000
Deposited: 2000
Current balance: 7000
Withdrawn: 3000
Current balance: 4000
Insufficient balance
'''

class BankAccount:
    def __init__(self,account_holder,balance):
        self.account_holder=account_holder
        self.__balance=balance

    def show_balance(self):
        print(f"your current account balance is : {self.__balance}")

    def deposit(self,amount):
        self.amount=amount

        if(self.amount<0):
            print("amount cannot be 0, please re-enter ")
        else:
            print(f"your deposited amount {self.amount}")
            self.__balance=self.__balance+self.amount

    def withdraw(self,amount):
        self.amount=amount

        if(self.amount>self.__balance):
            print("ensufficient amount ")
        else:
            print(f"your withdrawn amount {self.amount}")
            self.__balance=self.__balance-self.amount

acc = BankAccount("Piyush", 5000)

acc.show_balance()
acc.deposit(2000)
acc.show_balance()
acc.withdraw(3000)
acc.show_balance()
acc.withdraw(6000)


# ----------------------------------- proper valadited code
class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.__balance = balance   # private variable

    def show_balance(self):
        print(f"Current balance: {self.__balance}")

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive")
        else:
            self.__balance += amount
            print(f"Deposited: {amount}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive")
        elif amount > self.__balance:
            print("Insufficient balance")
        else:
            self.__balance -= amount
            print(f"Withdrawn: {amount}")
