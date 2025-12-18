prices=[]
foods=[]
total=0 

while True:
  food = input("Enter the Food:(q for quit): ")
  if food.lower() == "q":
    break
  else:
    price = int(input("Enter the price in Rupee: "))
    foods.append(food)
    prices.append(price)
for food in foods:
  print(food,end=" ")
for price in prices:
  total += price
print()
print(f"Your Total Bill is :{total}")