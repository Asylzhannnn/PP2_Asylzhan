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
print(trapezoid_area(eni,biiktyk,uzyndygy))