#Inheritance 
# Inheritance allows a child class to use the properties and methods of a parent class.
# It helps in code reusability and follows the IS-A relationship.

class Animal:
    def eat(self):
        print("Animal eats food")

class Dog(Animal):
    def bark(self):
        print("Dog barks")
d = Dog()
d.bark()    # own method
d.eat()     # inherited

# Types of Inheritance in python

# 1>Single Inheritance
class Parent:
    def show(self):
        print("Parent class")

class Child(Parent):
    pass





#Multilevel inheritance
# child => Parent => GrandParent

class GrandParent:
    def gp(self):
        print("Grandparent")

class Parent(GrandParent):
    def p(self):
        print("Parent")

class Child(Parent):
    def c(self):
        print("Child")
obj = Child()
obj.gp()
obj.p()
obj.c()

#Multiple Inheritance
# child Inherits from mutiple parents
class Father:
    def skill1(self):
        print("Driving")

class Mother:
    def skill2(self):
        print("Cooking")

class Child(Father, Mother):
    pass
c = Child()
c.skill1()
c.skill2()

# Hierarchical Inheritance
# One parent → multiple children
class Vehicle:
    def fuel(self):
        print("Uses fuel")

class Car(Vehicle):
    pass

class Bike(Vehicle):
    pass
