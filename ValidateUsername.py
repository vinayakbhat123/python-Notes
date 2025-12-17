userName= input("Enter the UserName: ")

if len(userName)>10:
  print("Length must not be greater then 10")
elif not userName.find(" ")== -1:
  print("username can't includes spaces")
else:
  print(f"Welcome: {userName}")