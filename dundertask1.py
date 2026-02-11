# class Book:
#     def __init__(self, title, author, price):
#         self.title = title
#         self.author = author
#         self.price = price

#     def __str__(self):
        
#         return f"'{self.title}' by {self.author} costs ₹{self.price}"

#     def __repr__(self):
#         return f"Book('{self.title}', '{self.author}', {self.price})"
# b1 = Book("Python Basics", "Guido", 500)
# b2 = Book("AI Fundamentals", "John", 800)
# print(b1,b2)       
# print(b1, b2)   


#task 2

# class Mobile:
#     def __init__(self, brand, model, price):
#         self.brand = brand
#         self.model = model
#         self.price = price
#     def __eq__(self, other):
#         return self.brand == other.brand and self.model == other.model
# m1 = Mobile("Apple", "iPhone 15", 80000)
# m2 = Mobile("Apple", "iPhone 15", 85000)
# m3 = Mobile("Samsung", "S24", 75000)
# print(m1 == m2)   
# print(m1 == m3)   

#task 3

# class User:
#     def __new__(cls, *args, **kwargs):
#         print("Object is being created")
#         return super().__new__(cls)

#     def __init__(self, name):
#         print("Object is initialized")
#         self.name = name

# u = User("Vinutha")

# task 4

# class DatabaseConnection:
#     def __enter__(self):
#         print("Database Connected")
#         return self

#     def __exit__(self, exc_type, exc_value, traceback):
#         print("Database Closed")
# with DatabaseConnection():
#     print("Performing Query...")

# task 5

# class Calculator:
#     def __call__(self, a, b):
#         return a + b
# obj = Calculator()
# print(obj(10, 20))   

# task 6

# class ShoppingCart:
#     def __init__(self, items):
#         self.items = items

#     def __getitem__(self, index):
#         return self.items[index]

#     def __setitem__(self, index, value):
#         self.items[index] = value
# cart = ShoppingCart(["Milk", "Bread", "Eggs"])
# print(cart[0])      
# cart[1] = "Butter"
# print(cart.items)     

# task 7

# class Session:
#     def __del__(self):
#         print("Session Ended")
# s = Session()
# del s

# task 8

# class Library:
#     def __init__(self, books):
#         self.books = books
#     def __contains__(self, item):
#         return item in self.books
# library = Library(["Python", "AI", "ML"])
# print("Python" in library)  
# print("Java" in library)     

# task 9

# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#     def __gt__(self, other):
#         return self.salary > other.salary
#     def __lt__(self, other):
#         return self.salary < other.salary
# e1 = Employee("A", 50000)
# e2 = Employee("B", 70000)
# print(e1 > e2)   
# print(e1 < e2)   

# task 10

# class Counter:
#     def __init__(self, start, end):
#         self.current = start
#         self.end = end
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.current <= self.end:
#             value = self.current
#             self.current += 1
#             return value
#         else:
#             raise StopIteration
# for i in Counter(1, 5):
#     print(i)






