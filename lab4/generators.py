#exercise 1

def square(N):
    for i in range(1,N+1):  #вклюячая N
        yield i**2
N=int(input("N:"))
squares=square(N) #generation
print(list(squares))     

#exercise 2
   
   
   