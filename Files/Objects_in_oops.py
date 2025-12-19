#Objects  => Instance if the class
# 🔹 Object in OOP (Python)
# In Object-Oriented Programming (OOP), an object is a real-world entity created from a class.
# It represents data (attributes) and behavior (methods) together.


# 🔹 What does an Object contain?

# Attributes → variables inside class

# Methods → functions inside class

class Student:
  def __init__(self,name,age):
    self.name = name
    self.age = age

  def display(self):
    print(f"{self.name} : {self.age} year old")
#creating objects
obj = Student("Vinayak",10)
obj.display()
print(obj)

#Example
class User:
    def __init__(self, username):
        self.username = username

    def is_admin(self):
        return self.username == "admin"

u1 = User("admin")
u2 = User("vinayak")

print(u1.is_admin())
print(u2.is_admin())

#Example 2
class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def show(self):
        print(self.username, self.email)

user1 = User("vinayak", "v@gmail.com")
user1.show()




# 🔹 What is __init__ in Object (Python OOP)?

# __init__ is a special method (constructor) in Python that is automatically called when an object is created.