#class methods
# A class method is a method that belongs to the class, not an instance, but can access class variables and methods.
# It is defined using the @classmethod decorator.

#syntax
class ClassName:
    @classmethod
    def method_name(cls, parameters):
        pass
        # code        
# @classmethod → decorator for class methods
# cls → reference to the class, similar to how self refers to the object

# 🔹 Interview One-Liner
# A class method is a method that belongs to the class, takes cls as the first parameter, and can access or modify class variables.

class Employee:
    company = "ABC Corp"  # class variable

    @classmethod
    def show_company(cls):
        print("Company:", cls.company)
Employee.show_company()   #Company ABC Corp
# e = Employee()
# e.show_company()


#Example 3
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, data):
        name, age = data.split("-")
        return cls(name, int(age))
p1 = Person.from_string("Vinayak-22")
print(p1.name,p1.age)

#Example 4
class Employee:
    company = "ABC Corp"

    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company

Employee.change_company("XYZ Ltd")
print(Employee.company)  # XYZ Ltd
