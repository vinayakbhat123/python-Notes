#Membership ops = used to test whether a value or variable is found in sequence(String,list,tuple and dictionary)
 # 1> in
 # 2>not in

   #  List 

# name = "vinayak Bhat"
# if "v" in name:
#   print("Char found in name")
# else:
#   print("Not Found")

# if "v" not in name:
#   print("Char found in name")
# else:
#   print("Not Found")

   #set

# students = {"vinayak","guru","madhavi"}
# student ="vinayak"
# if student not in students:
#   print(f"{student} is a student")
# else:
#   print(f"{student} is not a student")

   #dictionary

# students ={"abhi":"c",
#            "vinayak":"A",
#            "Guru":"A+",
#            "Koushik":"A+"}
# student = "vinayak"
# if student  in students:
#   print(f"{student} grade is: {students[student]}")
# else:
#   print(f"{student} is not a student")


email="vinayakbhat@gmail.com"

if "@" in email and "." in email:
  print("valid email")
else:
  print("Invalid  email")