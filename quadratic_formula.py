import math
import cmath

def coefficient(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    
    if discriminant < 0:
     x1 = (-b + cmath.sqrt(discriminant)) / (2 * a)
     x2 = (-b - cmath.sqrt(discriminant)) / (2 * a)
    else:
     x1 = (-b + math.sqrt(discriminant)) / (2 * a)
     x2 = (-b - math.sqrt(discriminant)) / (2 * a)
    
    return x1, x2

#(1)
a =1
b =-6
c =9
print(coefficient(a,b,c))

#(2)
a =1
b =2
c =-8
print(coefficient(a,b,c))

#(3)
a =8
b =-6
c =-35
print(coefficient(a,b,c))

#(4)
a =1
b =0
c =1
print(coefficient(a,b,c))
