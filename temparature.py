unit = input("Enter the temprature in Celcius or Faranheit (C/F): ")
temp = float(input("Enter the temparature"))



if unit == "C":
  temp = round((9 * temp)/5 + 32,1)         #  (°C * 9/5)+32  = °F    formula
  print(f"The Temparature in Faranheit is {temp}°F")     # ALT + 0176  = °  
elif unit == "F":
  temp = round((temp - 32)* 5/9,1)          #  (°F - 32)* 5/9 = °C   formula
  print(f"The Temparature in Celcius is: {temp}°C")     # ALT + 0176  = °  
else:
  print(f"Invalid {unit}")