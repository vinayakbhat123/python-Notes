# *args =>  allow to pass multiple arguments 
# ** kwargs =? allow to pass multiple arguments * unpacking operator

       # *args 
# def display(*args):
#   for arg in args:
#     print(arg, end=" ")
# display("I","am","Vinayak","Bhat","from","yellapura")


#**kwargs

def address(**kwargs):
  if "city" in kwargs:
    print(f"city is :{kwargs.get("city")}")

  for key,value in kwargs.items():
    print(f"{key}:{value}")
    
address(country="India",
        state="karnataka",
        city="yellapura")