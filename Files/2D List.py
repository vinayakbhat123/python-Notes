Names = {"Vinayak","Guru","Madhavi"}
LastName = {"Bhat","Hegde","Bhat"}
Place = {"Yellapur","Sirsi","Bangalore"}

collection = (Names,LastName,Place)
for i in collection:
  for j in i:
    print(j,end=" ")
  print()