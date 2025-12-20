# super()
# super() is used to call methods (especially __init__) of the parent class from a child class.
# It is very important in inheritance, especially when constructors are involved.

class Person:
    def __init__(self, name,age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name,age, marks):
        super().__init__(name,age)   # calls Person's constructor
        self.marks = marks
s = Student("Vinayak",18, 90)
print(s.name, s.marks,s.age)

# Multiple Inheritance
class Father:
    def __init__(self):
        print("Father")

class Mother:
    def __init__(self):
        print("Mother")

class Child(Father, Mother):
    def __init__(self):
        super().__init__()
        print("Child")
print(Child.mro())
c = Child()
