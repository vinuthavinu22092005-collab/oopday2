#banking system
class BankAccount:
  account_holder_name="unknown"
  _account_type="Savings"
  def __init__(self,pin):
    self.__pin=pin
    self.__balance=0
  
  def set_pin(self,newpin):
    self.__pin=newpin
    print("Pin updated successfully")
  def verify_pin(self,pin):
    return pin==self.__pin
  def get_balance(self,pin):
    if self.verify_pin(pin):
      return self.__balance
    else:
      print("Invalid pin!")
      return None
  def set_balance(self,pin,amount):
    if self.verify_pin(pin):
      self.__balance=amount
      print("Balance updated successfully",self.__balance)
    else:
      print("Invalid pin enter valid one")
bank=BankAccount("1234")  
bank.account_holder_name="vinutha"
print("Account Holder Name:",bank.account_holder_name)
print("account pin:",bank._BankAccount__pin)
bank.set_pin("5678")
print(" updated account pin:",bank._BankAccount__pin)
print("Current balance is:",bank.get_balance("5678"))
bank.set_balance("1234",5000)
