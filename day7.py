# class parent:
#   def __init__(self,a,b):
#     self.a=a
#     self.b=b
#   def add(self):
#     return self.a+self.b
# class child(parent):
#   def __init__(self,a,b):
#     super().__init__(a,b)
#     print("Parent sum:",super().add())
    
#   def add(self):
#     return self.a+self.b
# ch1=child(10,20)
# print(ch1.add())

#method overloading
class Calculator:
    def add(self,a,b):
        return a + b

    def add(self,a,b,c):
        return a + b + c
calc = Calculator()
print(calc.add(10, 20, 30))  # Output: 60