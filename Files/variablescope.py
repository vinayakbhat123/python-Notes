#variable scope 

# Variable scope defines where a variable can be accessed in a program.

# Python follows LEGB Rule for scope resolution.

# 🧠 LEGB Rule

# L – Local (inside a function)

# E – Enclosing (nested function)

# G – Global (outside all functions)

# B – Built-in (Python keywords/functions)


## Local scope  => accessible only inside funtion

def my_func():
    x = 10   # local variable
    print(x)

my_func()
# print(x) ❌ Error


## global scope =>Accessible everywhere
x= 11
def show():
    print(x)
show()


## Local vs Global variables

x= 15
def change():
    x=8
    print(f"{x} local")
change()
print(x)


#using global keyword
x=5
def new_change():
    global x
    x= 1
new_change()
print(f"{x} is a global ")

#Enclosing scope  =>Inner function can access outer variable.
def outer():
    x = "outer"

    def inner():
        print(x)
    inner()
outer()

#using nonlocal keyword to modify enclosing vaiable
def outer():
    x = "outer"
    def inner():
        nonlocal x
        x = "inner"
    inner()
    print(x)
outer()


