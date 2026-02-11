from abc import ABC, abstractmethod
class Animal(ABC):
  @abstractmethod
  def sound(self):
    pass
  def sleep(self):
    print("sleeping")
class Dog(Animal):
  def sound(self):
    print("Bark")
class cat(Animal):
  def sound(self):
    print("meow")
class Cow(Animal):
  def sound(self):
    print("moo")
d=Dog()
d.sound()
c=cat()
c.sound()
cow=Cow()
cow.sound()
c.sleep()
cow.sleep()
d.sleep()