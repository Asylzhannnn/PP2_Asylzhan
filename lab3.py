
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


        