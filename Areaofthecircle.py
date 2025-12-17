# calculate the area of traingle  formula  c = pi*r^2
import math
radius = float(input("Enter the radius of the circle "))
area= math.pi * pow(radius,2)
print(f"The area of a circle is {area}cm^2")

# calculate hypothosis of triangle  
a = float(input("Enter the side of A: "))
b = float(input("Enter the side of B: "))
c = math.sqrt(pow(a,2)+pow(b,2))
print(f"side of c is: {c}")