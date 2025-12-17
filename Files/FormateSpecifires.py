#flags specifires =>  {value:flag}  formate the value based on the what are inserted

a=300000.5454
b=-800.232
c= 08089.3233
print(f"The value is:{a:.2f}")  # 2 decimal places
print(f"The value is:{a:10}")  #10 spaces takes to display text
print(f"The value is:{c:010}") # zero added left side
print(f"The value is:{a:>10}")# take 10 spaces right side and justify
print(f"The value is:{a:+}") # take + left side
print(f"The value is:{a:,}")  #The value is:300,000
print(f"The value is:{a:+,.2f}")   #The value is:+300,000.55