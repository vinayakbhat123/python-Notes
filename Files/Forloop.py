#forloop
for x in range(1,5):
  print(x ,end="")

for x in reversed(range(1,5)):
  print(x)

for x in (range(1,5,2)):
  print(x)

numbers = "1231-565-464-44"
for x in numbers:
  print(x )

for x in range(1,21):
  if x== 13:
    continue
  elif x== 17:
    break
  else:
     print(x)
  