class Payment:
  def pay(self,amount):
    print("Payment of",amount,"is successful")
class GooglePay(Payment):
  def pay(self,amount):
    print("Google Pay payment of",amount,"is successful")
class PhonePe(Payment):
  def pay(self,amount):
    print("PhonePe payment of",amount,"is successful")
class CreditCard(Payment):
  def pay(self,amount):
    print("Credit Card payment of",amount,"is successful")

payment1=GooglePay()
payment2=PhonePe()
payment3=CreditCard()
payment1.pay(1000)
payment2.pay(2000)
payment3.pay(3000)