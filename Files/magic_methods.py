#magic methods

# 🔹 What are Magic Methods?
# Magic methods are special methods in Python that:
# Start and end with double underscores
# Are automatically called by Python
# Allow you to customize object behavior
# 📌 They are also called dunder methods
# (dunder = double underscore)

# 🔹 Basic Definition (Interview-Ready)
# Magic methods are special methods that allow classes to define how objects behave with built-in Python operations.

# 1> __init__ Constructor
class Person:
    def __init__(self, name):
        self.name = name

p = Person("Vinayak")    #Automatically runs when Person() is called.
print(p)

# 2> __str__ constructor
class Person:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f"Person name is:{self.name}"

p = Person("Vinayak")    #Automatically runs when Person() is called.
print(p)

# 3> __len__ constructor
# called by len()
class Course:
    def __init__(self, students):
        self.students = students

    def __len__(self):
        return len(self.students)
c = Course(["A", "B", "C"])
print(len(c))

# __add__ constructor
# called by using +

class Addition:
    def __init__(self,name,a):
        self.name = name
        self.a = a
    def __add__(self,other):
        return self.a + other.a
    def __lt__(self,other):          # __lt__   (less then) dunder method
        return self.a < other.a
    def __gt__(self,other):
        return self.a > other.a
    def __eq__(self, other):
        return self.a == other.a
    def __contains__(self,word):
        return word in self.name 
    def __getitem__(self,word):
        if word == "vinayak":
            return self.name
        else:
            return "Not Found"
p1 = Addition("vinayak Bhat",10)
p2 = Addition("Guru bhat",20)
print(p1+p2)
print(p1<p2)
print(p1>p2)
print(p1 == p2)
print("vinayak" in p1)
print(p1["vinayak"])
        

# Magic Methods with Built-in Functions
# Built-in Function    =>	  Magic Method
# print(obj)	         =>   __str__()
# len(obj)	           =>   __len__()
# obj + other	         =>   __add__()
# obj == other	       =>   __eq__()
# str(obj)	           =>   __str__()