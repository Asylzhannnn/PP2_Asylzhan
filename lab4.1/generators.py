#exercise 1

def square(N):
    for i in range(1,N+1):  #вклюячая N
        yield i**2
N=int(input("N:"))
squares=square(N) #generation
print(list(squares))     

#exercise 2
   
def gen(n):
    for i in range(0,n+1):     #range(0, n+1, 2) если указать шаг 2 то ай деленное на два не нужно
        if i % 2 == 0:
            yield i
n = int(input("n:"))
mygen = gen(n)
for x in mygen:
    print(x)
    
#exercise 3

def gen(n):
    for i in range(0,n+1):    #range(0, n + 1, 12):  # Шаг 12, т.к. LCM(3,4) = 12
        if i % 3 == 0 and i % 4 == 0:
            yield i
        
n = int(input())
mygen = gen(n)
for x in mygen:
    print(x)    


#exercise 4

def squares(a,b):
    for i in range(a,b+1):
            yield i * i
a = int(input())
b = int(input())
mygen = squares(a,b)
for x in mygen:
    print(x) 
    
#exercise 5

def gen(n):
    for i in range(n, -1, -1):
        yield i 
n = int(input())
mygen = gen(n)
for x in mygen:
    print(x)       