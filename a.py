#PYTHON HOME 1
print("Hello Yeralim!") 

#PYTHON GET STARTED 2
import sys

print(sys.version)


#PYTHON SYNTAX 3
if 5 > 2:
  print("Five is greater than two!")
# the indentation in Python is very important

if 6 > 2:
 print("Six is greater than two!") 
if 6 > 2:
        print("Six is greater than two!") 
       #You have to use the same number of spaces in the same block of code, otherwise Python will give you an error 

x = 4537
y = "Hello, World!"

print(x)
print(y)

#PYTHON COMMENTS 4

print("Hello, World!") #This is a comment
#to write whole sentence of text comments we use triple quotes
"""hello my name is Asylzhan hbjwblubcbcukbubvjcvgvgbchbjkcvkjbhbjcbjbbhvcj
jdcnjdbjbjbcbbsjcnjnnnncncklnnb
ksnnncndnn"""

#PYTHON VARIABLES 5

x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)    # answer will be Sally 

#casting 5.1
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

#get the type 5.2
x = 5
y = "John"     #You can get the data type of a variable with the type() function.
print(type(x))
print(type(y)) #answ:<class 'int'>
               #answ:<class 'str'>
#case sensetive 5.3
a = 4
A = "Sally"
#A will not overwrite a

#variable names 5.4
"""A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
A variable name cannot be any of the Python keywords."""
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

#variable multiple variables 5.5
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)  #note that the number of variables matches the number of values, or else you will get an error.

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits

print(x)
print(y)
print(z)  #it is called unpack a list

#variables output 5.6
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)  #you can do it also without +


x = 5
y = "John"
print(x, y) 
"""In the print() function, when you try to combine a string
and a number with the + operator, Python will give you an error:"""

#variable global 5.7
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)  
"""answ: Python is fantastic
         Python is awesome"""
         
#PYTHON DATA TYPES 6
x = ["apple", "banana", "cherry"]

#display x:
print(x)

#display the data type of x:
print(type(x)) 


#PYTHON NUMBERS 7
x = 1
y = 2.8
z = 1j

print(type(x))
print(type(y))
print(type(z))


#PYTHON CASTING 8

x = str("s1") # x will be 's1'
y = float(2.8)   # y will be 2.8
z = int(2.8) # y will be 2


#PYTHON STRING 9
         
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

#string slicing 9.1
b = "Hello, World!"
print(b[2:]) #answ:llo, World!

l = "Hello, World!"
print(l[2:5]) #answ:llo

#string modify 9.2

a = "Hello, World!"
print(a.upper()) #HELLO, WORLD!

a = "Hello, World!"
print(a.lower()) #hello world!

a = " Hello, World! "
print(a.strip()) #(answer:Hello, World!) The strip() method removes any whitespace from the beginning or the end:
 
a = "Hello, World!"
print(a.replace("H", "J")) #Jello, World!

a = "Hello, World!"
b = a.split(",")
print(b)
#answ:['Hello', ' World!']

#string concatenation 9.3
a = "Hello"
b = "World"
c = a + " " + b
print(c)
#answ:
a = "Hello"
b = "World"
c = a + " " + b
print(c)
#Hello World

#format strings 9.4


age = 36
txt = f"My name is John, I am {age}"
print(txt)
#answ:My name is John, I am 36

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt) #The price is 59.00 dollars

txt = f"The price is {20 * 59} dollars"
print(txt)
#The price is 1180 dollars

#string escape character 9.5


txt = "We are the so-called \"Vikings\" from the north."
print(txt) 
#We are the so-called "Vikings" from the north.

txt = "This will insert one \\ (backslash)."
print(txt) #This will insert one \ (backslash).

txt = "Hello\nWorld!"
print(txt) #Hello
           #World!

txt = "Hello\tWorld!"
print(txt) #Hello   World!

#This example erases one character (backspace):
txt = "Hello \bWorld!"
print(txt) #HelloWorld


#A backslash followed by three integers will result in a octal value:
txt = "\110\145\154\154\157"
print(txt) #Hello

                      
#A backslash followed by an 'x' and a hex number represents a hex value:
txt = "\x48\x65\x6c\x6c\x6f"
print(txt) #Hello

txt = "Hello\rWorld!"
print(txt) 
"""Hello
World!"""

#that is all                      