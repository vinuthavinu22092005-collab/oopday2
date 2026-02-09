class BankAccount:
    def __init__(self,account_holder,balance):
        self.account_holder=account_holder
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
        print("deposited amount is",amount)
    def withdraw(self,amount):
        if self.balance>=amount:
            self.balance-=amount
            print("withdrawn amount is",amount)
        else:
            print("insufficient balance")
    def display_balance(self):
        print("balance is",self.balance)
class SavingsAccount(BankAccount):
    def __init__(self,account_holder,balance,interest_rate):
        super().__init__(account_holder,balance)
        self.interest_rate=interest_rate
    def add_interst(self):
        interest=self.balance*self.interest_rate/100
        self.balance+=interest
        print("interest added is",interest)
class CurrentAccount(BankAccount):
    def __init__(self,account_holder,balance,overdraft_limit):
        super().__init__(account_holder,balance)
        self.overdraft_limit=overdraft_limit
    def withdraw_with_overdraft(self,amount):
        if amount<=self.balance+ self.overdraft_limit:
            self.balance-=amount
            print("withdrawn amount is",amount)
        else:
            print("exceeded overdraft limit")
Sa=SavingsAccount("vinutha",500,5)
Sa.deposit(500)
Sa.withdraw(300)
Sa.add_interst()
Sa.display_balance()

Ca=CurrentAccount("vinutha",1000,500)
Ca.withdraw_with_overdraft(1200)
Ca.display_balance()
    
        