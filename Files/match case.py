#matchcase 
#syntax
# match value:
#     case pattern1:
#         # code
#     case pattern2:
#         # code
#     case _:
#         # default case

day = 3

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case _:
        print("Invalid day")


#using variable (pattern binding)
value = 10
match value:
    case x if x > 0:
        print("Positive number")
    case x if x < 0:
        print("Negative number")
    case _:
        print("Zero")

#matching in dictionaries

user = {"role": "admin", "active": True}
match user:
    case {"role": "admin", "active": True}:
        print("Active Admin")
    case {"role": "admin", "active": False}:
        print("Inactive Admin")
    case _:
        print("Normal User")
