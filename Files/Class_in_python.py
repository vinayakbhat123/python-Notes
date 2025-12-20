# class
# A class in Python is a blueprint for creating objects.
# It groups data (variables) and behavior (functions) together.

#syntax
class Classname:
  def __init__(self):
    pass

#Example
class Student:
  address = "yellapura"
  def __init__(self,name,age):
    self.name= name   #Attributes or Instance variable
    self.age = age
  def show(self):     #Methods or functions
    print(f"Hello i am {self.name} and {self.age} from {Student.address}")

obj = Student("Vinayak",15)
obj.show()

#Exmple2
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def show_balance(self):
        print("Balance:", self.balance)

acc = BankAccount(1000)
acc.deposit(500)
acc.show_balance()

#Example 3
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def info(self):
        print(self.brand, self.model)
c1 = Car("Tata", "Nexon")
c2 = Car("Hyundai", "Creta")

c1.info()
c2.info()
