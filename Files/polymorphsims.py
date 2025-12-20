# What is Polymorphism in Python?
# Polymorphism means “many forms.”
# In programming, it means the same method name behaves differently depending on the object.


# 🔹 One-Line Interview Answer ⭐
# Polymorphism allows the same method to perform different actions based on the object calling it.


class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

class Cat(Animal):
    def sound(self):
        print("Cat meows")

animals = [Animal(),Dog(), Cat()]

for a in animals:
    a.sound()


#Example  polymorphism with super()
class Employee:
    def work(self):
        print("Employee works")

class Manager(Employee):
    def work(self):
        super().work()
        print("Manager manages team")
