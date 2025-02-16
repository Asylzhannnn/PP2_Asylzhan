#exercise 1

def converting(degree):
    return degree*3.14/180
degree=int(input("Degree is :"))
print(f"That {degree} in radians is {converting(degree)}")    


#exercise 2

def trapezoid_area(eni,uzyndygy,biiktyk):
    return (eni+uzyndygy)*biiktyk/2
eni=int(input("Eni :"))
uzyndygy=int(input("Uzyndygy :"))
biiktyk=int(input("Biiktygy :"))
print(trapezoid_area(eni,uzyndygy,biiktyk))


#exercise 3

import math
def polygon_area(n,l):
    return (n*l*l)/(4 * math.tan(math.pi / n))
n=int(input("Numside:"))
l=float(input("Length:"))
print("The area of polygon:",polygon_area(n,l))



#exercise 4

def area_parallelogramm(h,b):
    return h*b
b = float(input("Length of base: "))
h = float(input("Height of parallelogram: "))
s=area_parallelogramm(h,b)
print(f"The parallelograms area is {s:.1f}")