#nestedloop => a loop in another loop
# for i in range(3):
#   for a in range(1,10):
#     print(a,end="-")
#   print()
rows= int(input("Enter the rows: "))
columns= int(input("Enter the colums: "))
symbol = input("Enter the symbol to use: ")
for i in range(rows):
  for a in range(columns):
    print(symbol,end="-")
  print()