
"""CLASS EXERCISES"""
#class 1
class String:
    def __init__(self):
        self.text = ""

#get-принимать , so we are getting string from customer(пользователя)
    def getString(self):
        self.text = input("sentence: ")

#here we are printing our string in upper case
    def printString(self):
        print("sentence in uppercase:", self.text.upper())

# creting classs and bringing methods
mysentence = String()
mysentence.getString()
mysentence.printString()
  
#class 2  
  
class Shape():
    def area(self):
        return 0  #shape's area is 0
class Square(Shape):
    def __init__(self,length):
        self.length=length # saving length 
    def area(self):
        return self.length ** 2 #s=a**2
a = float(input("a:")) # getting length from user
mysquare=Square(a)     # creating object square
print("S:",mysquare.area()) 
myshape=Shape()        #creating object shape
print("Other S:",myshape.area())

#class 3

class Shape():
    def area(self):
        return 0
class Rectangle(Shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width  
    def area(self):
        return self.length*self.width #findind it by formula
#giving numbers for a and b
length=float(input("a:"))
width=float(input("b:"))
myrectangle=Rectangle(length,width)
print("S:",myrectangle.area())          


#class 4

class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        
    def show(self):
        print(f"coordinates:({self.x},{self.y})")
        
    def move(self,x1,y1):
        self.x=x1
        self.y=y1
        
    def dist(self,point2):
        dx=self.x-point2.x
        dy=self.y-point2.y
        distance=(dx**2+dy**2)**0.5
        return distance
a=float(input("x:"))
b=float(input("y:"))
point1=Point(a,b)
point2=Point(a,b)

point1.show()
c=float(input("x1:"))
d=float(input("y1:"))

point1.move(c,d)
point1.show()
distance=point1.dist(point2)
print(f"Distance between 1 and 2 points: {distance}")
        
        
#class 5        
        
class Bank:
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance   
    def deposit(self,amount):
        self.balance+=amount
        print(f"Ypu added {amount} money. In your deposit now has: {self.balance}")
    def withdraw(self,amount):
        if amount>self.balance:
            print("You don't have enough money")
        else:
            self.balance-=amount
            print(f"You take {amount} from deposit.Initial balance:{self.balance} ")
    def show_balance(self):
        print(f"Current balance: {self.balance}")
    def show_owner(self):
        print(f"Owner is {self.owner}")   
        
bank=Bank("Asylzhan",500)
bank.show_balance()
bank.show_owner()
bank.deposit(47135)
bank.withdraw(50000)
bank.withdraw(47500)
bank.show_balance()   
        
   
#class 6

class Prime:
    def __init__(self, numbers):
        self.numbers = numbers

    def is_prime(self, num):
        """checks the number """
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def filter_prime_numbers(self):
        """filtres and leaves prime numbers"""
        return list(filter(self.is_prime, self.numbers))  # Вызываем is_prime через self
n = int(input("num of numbers: "))
mylist = list(map(int, input("numbers: ").split()))
prime_filter = Prime(mylist)
print("Prime numbers:", prime_filter.filter_prime_numbers())
          
                    

"""FUNCTION 1"""

#functions 1

def convert(grams):
    return grams*28.3495231  #our coef for exercise
grams=float(input("g:"))  #users number for grams
print("Weight:",convert(grams)) # final result in ounces



#functions 2

def conversion(F):
    return(5/9)*(F-32)  #formula of conversion
F=float(input("fahrenheit: "))
print("From F to C is ",conversion(F))


#functions 3

def solve(head,leg):
    for chikens in range(head+1):
        rabbits=head-chikens
        if chikens*2+rabbits*4==leg:
            return rabbits,chikens
    return "no right answer"
chikens,rabbits=solve(35,94)
print(f"Chikens:{chikens}, Rabbits:{rabbits}")  
  

#function 4

def is_prime(num):
    if num < 2:     #Check if the number is less than 2
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def filter_prime(numbers):   #Filter the list of numbers, keeping only primes
    return list(filter(is_prime, numbers))

numbers_str = input("enter list: ")
numbers_list = list(map(int, numbers_str.split()))

prime_numbers = filter_prime(numbers_list)
print("Prime numbers:", prime_numbers)            
            

#function 5

def permutations(some):
    n = len(some) #определяем длину n
    for i in range(n):
        for j in range(n): #количество строк i n раз j n раз
            print(some[(j-i)], end=" ") #обращение к символам могут быть отрицательными
        print()

k = str(input("word:"))
permutations(k)


#function 6

sentence = input("Your sentence: ")
words = sentence.split()  #we separate sentense for words
words.reverse()           # reversing list of words
reversed_sentence = ' '.join(words)  #creating sentence from reversed list
print(reversed_sentence)
         
            
#function 7

def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True #checks each number and the next number
    return False
has_33([1, 3, 3])
print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3]))
            
#function 8

def spy_game(nums):
    code = [0, 0, 7]
    code_index = 0    

    for num in nums:
        if num == code[code_index]:
            code_index += 1
#if it matches the current expected number, move to the next number 
        if code_index == len(code):  # Found all numbers in order
            return True
    return False

#function 9

import math
def volumespher(radius):
    V=(4*math.pi*(radius**3))/3
    return V
    
radius=float(input("radius:"))
print(volumespher(radius))

#function 10

def unique(mylist):
    count_dict = {}
    for item in mylist:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
    #how many times each number appears
    result = [item for item in mylist if count_dict[item] == 1]
    return result
#Input
n = int(input("Enter the number of elements: "))
mylist = []
for i in range(n):
    number = int(input(f"Enter number {i+1}: "))
    mylist.append(number)
print("Unique elements:", unique(mylist))

#function 11

def palindrom(text):
    if text==text[::-1]: #if text equal to its reversed form
        print("YES")
    else:
        print("NO")
#[::-1] means "start from the end, move backward by 1
text = input("text: ")
palindrom(text)

#function 12
def histogram(nums):
    for num in nums:
        print('*' * num)
# * multiplied by the number
   

#function 13

from random import randint

def guessanumber():
    print("Hello! What is your name?")
    name = input("name:")
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    number = randint(1,20)
    sum = 0
    atempt = True
    while atempt:
        guess = int(input("Take a guess: "))
        sum+=1
        if guess == number:
            atempt = False
            print(f"Good job, {name}! You guessed my number in {sum} guesses!")
            break
        if guess>number:
            print("Your guess is too high.")
        else:
            print("Your guess is too low")


#function 14

from random import randint
def guessanumber():
    print("Hello! What is your name?")
    name = input()
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    number = randint(1,20)
    sum = 0
    run = True
    while run:
        guess = int(input("Take a guess: "))
        sum+=1
        if guess == number:
            run = False
            print(f"Good job, {name}! You guessed my number in {sum} guesses!")
            break
        if guess>number:
            print("Your guess is too high.")
        else:
            print("Your guess is too low")
guessanumber()
def randomator(start, end, length):
    arr=[randint(start, end)for i in range(length)]
    print(arr)
randomator(1,10,10)
guessanumber()    
                    
"""FUNCTIONS 2"""

movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]
#functions 2(1)
def imdb(movies):
    name=input("name:")
    for movie in movies:
        if movie["name"]==name:
            if movie["imdb"]>5.5:
                return True
    return False
print(imdb(movies))

#functions 2(2)
def score(movies):
    result =[]  #creating empty list for films with high rating
    for movie in movies: #try all films
        if movie["imdb"]>5.5: #if  film has rating>5.5
            result.append(movie)#we add it to our list
    return result        # return to new list(filtered list)
print(score(movies))

#functions 2(3)
def category(movies,name): #function brings name of category
     result=[]
     for movie in movies:
         if movie["category"]==name:
             result.append(movie)
     return result
name=str(input("Category name: ")) #user's choice
print(category(movies,name))       #bring films with that category    

#functions 2(4)

def average_imdb(movies):
    # to get list of IMDB rating we use 
    scores = [movie["imdb"] for movie in movies]
    avg_score = sum(scores) / len(scores)
    return avg_score
print("Средний рейтинг IMDB:", average_imdb(movies))


#functions 2(5)

def average_imdb_by_category(movies, category):
    # Filter movies if it belongs category
    filtered_movies = [movie["imdb"] for movie in movies if movie["category"] == category]
    if len(filtered_movies) == 0:
        return 0  #если не нашли фильм в категории 
    # Calculate the average IMDB score
    return sum(filtered_movies) / len(filtered_movies)
category_input = input("category: ")
average_score = average_imdb_by_category(movies, category_input)
print(f"Average IMDB score '{category_input}': {average_score:.2f}")

        