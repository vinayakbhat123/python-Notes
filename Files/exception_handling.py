# #exception handling
# Exception handling lets your program handle errors gracefully instead of crashing.


# syntax
# try:
#     code that may cause error
# except ExceptionType:
#     code to handle error
def divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"
print(divide(10, 2))
print(divide(10, 0))


#Example 3
def open_file():
    try:
        f = open("test.txt", "r")
        print(f.read())
    except FileNotFoundError:
        print("File not found")
    finally:
        print("Execution finished")
open_file()


#Example 4
def check_age(age):
    if age < 18:
        raise ValueError("Age must be 18 or above")
    return "Access granted"
check_age(90)


# Example 4
def get_element(lst, index):
    try:
        return lst[index]
    except IndexError:
        return "Index out of range"
get_element("hello",90)