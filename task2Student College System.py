class Student:
  college_name = "ABC College"
  def __init__(self, name, roll_no):
    self.name = name
    self.roll_no = roll_no
  @classmethod
  def change_college(cls, new_name):
    cls.college_name = new_name
  
  @staticmethod
  def is_pass(marks):
    return "Pass" if marks >= 35 else "Fail"
  def display(self):
    print(f"Name: {self.name}")
    print(f"Roll No: {self.roll_no}")
    print(f"College: {self.college_name}")
    print()

student1 = Student("Alice", 101)
student2 = Student("Bob", 102)
student1.display()
student2.display()
Student.change_college("XYZ College")
student1.display()
student2.display()
print(Student.is_pass(45))
print(Student.is_pass(30))