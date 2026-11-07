class Employee:
    def __init__(self, name: str, salary: int):
        self.name = name
        self.salary = salary

    def get_details(self):
        return f"Name: {self.name} and Salary: {self.salary}"

emp1 = Employee("John", 50000)
print(emp1.name)
print(emp1.salary)
print(emp1.get_details())

#Encapsulation
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance
        self.name = "John Doe"

    def deposit(self, amount):
        self.__balance += amount
    
    def withdraw(self, amount):
        self.__balance -= amount
    
    def get_balance(self):
        return self.__balance
    
account = BankAccount(1000)
print(account.name)
account.deposit(500)
account.withdraw(200)
print(account.get_balance())

#Super class and Subclass
class Animal:
    def __init__(self):
        print("Animal created")

class Dog(Animal):
    def __init__(self):
        super().__init__()
        print("Dog created")

dog = Dog()

# 3. Polymorphism
# Same method name, different behavior.
class Dog:
    def sound(self):
        return "Woof"
    
class Cat:
    def sound(self):
        return "Meow"
    
for animal in (Dog(), Cat()):
    #print(animal)
    print(animal.sound())

# Method Overriding - Child class replaces parent implementation.
class Animal:
    def sound(self):
        return "Animal sound"
    
class Dog(Animal):
    def sound(self):
        return "Bark"
    
dog = Dog()
print("Overriding:", dog.sound())

# Method Overloading - Same method name, different parameters or behavior.


# Abstract Class and Interface
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass
    
class Car(Vehicle):
    def start_engine(self):
        return "Car engine started"
    
car = Car()
print(car.start_engine())

# Static Method and Class Method
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b
    
print(MathUtils.add(5, 10))

class Employee:
    company = "ABC Corp"

    @classmethod
    def get_company(cls):
        return cls.company
    
print(Employee.get_company())

#__new__() vs __init__()
class Testi:
    def __new__(cls):
        print("Creating instance")
        return super().__new__(cls)
    
    def __init__(self):
        print("Initializing instance")
        

# Class method vs Static method
class Person:
    name = "Alice"
    
    @classmethod
    def get_name(cls):
        return cls.name

print(Person.get_name())

########################
class Person:
    def __init__(self, name):
        self.name = name

    @classmethod
    def from_full_name(cls, full_name):
        first_name = full_name.split()[0]
        return cls(first_name)
        
p = Person.from_full_name("Robet Martin")
print(p.name)

###########################
# Runtime polimorphism example
class Notification:
    def send(self):
        print("Send notification")
    
class SMSNotification(Notification):
    def send(self):
        super.send()
        print("Send SMS")
    
class EmaiNotification(Notification):
    def send(self):
        print("Send Email")

notifications = [SMSNotification, EmaiNotification]

for n in notifications:
    n.send()
