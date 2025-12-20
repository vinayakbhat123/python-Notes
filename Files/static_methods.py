#static Methods
# A static method is a method that belongs to a class, not to any object of the class.
# It cannot access instance variables (self) or class variables (cls) unless passed explicitly.
# Static methods are used for utility functions that make sense in a class but don’t need object-specific data.

#Example 1

# greet() needs object data (self.name) → instance method
# info() does not need object data → static method

class Person:
    def __init__(self, name):
        self.name = name
    
    def greet(self):      # instance method
        print(f"Hello, {self.name}")
    
    @staticmethod
    def info(msg):           # static method
        print(f"{msg} This is a Person class")
p = Person("Vinayak")                                          
p.greet()    # Hello, Vinayak
Person.info("hello")  # This is a Person class



#Example 2  => No object creation needed it saves memory
class Calculator:
    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def divide(a, b):
        if b != 0:
            return a / b
        else:
            return "Cannot divide by zero"
print(Calculator.multiply(5, 3))  # 15
print(Calculator.divide(10, 2))   # 5.0

