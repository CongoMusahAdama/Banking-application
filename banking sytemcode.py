
class Bank_Account:
    def __init__(self):
        self.balance=100
        print("Hello!!! Welcome to VEE'S Deposit & Withdrawal MOBILE APP")
        
    def deposit(self):
        print("Enter deposit amount:")
        amount=float(input("amount to be deposit:"))
        self.balance+=amount
        print("\n you deposited, amount:")
        

 
    def withdraw(self):
        amount = float(input("Amount to be withdrawn: "))
        if self.balance>=amount:
            self.balance+=amount
            print("\n You Withdrew:", amount)
        else:
            print("\n Insufficient balance  ")
 
    def display(self):
        print("\n Net Available Balance=",self.balance)
 

account=Bank_Account()
print(account.deposit())
print(account.withdraw())
print(account.display())


