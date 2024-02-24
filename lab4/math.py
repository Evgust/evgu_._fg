#Ex1

import math

x = int(input("degree: "))
z = x * (math.pi/180)
print("radian: ", z)

#Ex2

h = int(input("Height: "))
b1 = int(input("Base, first value: "))
b2 = int(input("Base, second value: "))
t = ((b1 + b2)*h)/2
print("Expected Output: ", t)

#Ex3
#A=n×a^2*1/4*cot(pi/n)
sides = int(input("Input number of sides: "))
l = int(input("Input the lenght of a side: "))
S = sides*pow(l, 2)*(1/4)*(1/(math.tan(math.pi/sides)))
print("The area of the polygon is: ", int(S))

#Ex4

lb = int(input("Length of base: "))
hp = int(input("Height of parallelogram: "))
Sp = lb*hp
print("Expected Output: ", float(Sp))
