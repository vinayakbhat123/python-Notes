#class variable
# In Python, class variables are variables that are shared by all objects (instances) of a class. 
# They belong to the class itself, not to any one object.

class Employee:
    count = 0   # class variable

    def __init__(self, name):
        self.name = name
        Employee.count += 1

e1 = Employee("A")
e2 = Employee("B")
e3 = Employee("C")

print("Total Employees:", Employee.count)
