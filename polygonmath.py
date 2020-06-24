from math import tan,pi
length=int(input("enter the length:"))
sides=int(input("enter the side:"))
area = sides * (length ** 2) / (4 * tan(pi / sides))
print("area of polygon is:",area)