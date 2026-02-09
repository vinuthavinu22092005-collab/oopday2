from abc import ABC, abstractmethod

class Vehicle(ABC):
  @abstractmethod
  def start_engine(self):
    pass

class Car(Vehicle):
  def start_engine(self):
    print("Car engine started with a smooth rumble")

class Bike(Vehicle):
  def start_engine(self):
    print("Bike engine started with a loud roar")

class Bus(Vehicle):
  def start_engine(self):
    print("Bus engine started with a heavy diesel sound")


car = Car()
car.start_engine()

bike = Bike()
bike.start_engine()

bus = Bus()
bus.start_engine()