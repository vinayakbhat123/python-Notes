# #decorators
# A decorator is a function that adds extra behavior to another function without modifying it.
# Why Use Decorators?
# ✔ Add functionality (logging, timing, authentication)
# ✔ Avoid code repetition
# ✔ Cleaner & reusable code
# ✔ Used heavily in Django, Flask, FastAPI

# Decorator Function

def my_decorator(func):
  def wrapper(*args,**kwargs):
    print("Before Function")
    func(*args,**kwargs)
    print("after function")
  return wrapper

#applying decorators
@my_decorator
def greet(name):
    print(f"Hello {name}")
greet("vinayak")


#Example 3

class MyDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self):
        print("Before")
        self.func()
        print("After")
@MyDecorator
def hello():
    print("Hello")
