#LAB 2
#BOOLEANS

print(10 > 9)
print(10 == 9)
print(10 < 9) 
'''True
   False
   False'''
   
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
  #answer: b is not graeter than a
  
print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))
    #answer:True True True 
    #Any list, tuple, set, and dictionary are True, except empty ones.
    #ny number is True, except 0
    
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))
"""False
False
False
False
False
False
False"""


class myclass():
  def __len__(self):
    return 0
myobj = myclass()
print(bool(myobj))
#False


def myFunction() :
  return True
if myFunction():
  print("YES!")
else:
  print("NO!")
#YES!

x = 200
print(isinstance(x, int))
#True
#Check if an object is an integer or not


#PYTHON OPERATIONS

x = 5
y = 2
print(x % y)
#answer: 1

x = 12
y = 5
print(x / y)
# 2.4

x = 2
y = 5
print(x ** y) #same as 2*2*2*2*2=32


x = 15
y = 2
print(x // y)
#a:7
#the floor division // rounds the result down to the nearest whole number

print(100 + ~3)
"""
Bitwise NOT has higher precedence than addition, and needs to be evaluated first.
The calculation above reads 100 + -4 = 96"""

#PYTHON LISTS

thislist = ["apple", "banana", "cherry"]
print(len(thislist)) #answer:3



mylist = ["apple", "banana", "cherry"]
print(type(mylist))#answer:<class 'list'>


thislist = list(("apple", "banana", "cherry"))
print(thislist)
#['apple', 'banana', 'cherry']
#note the double round-brackets


#Access items
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])
#answer:cherry

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
#['cherry', 'orange', 'kiwi']
#This will return the items from position 2 to 5.
#Remember that the first item is position 0,
#and note that the item in position 5 is NOT included



thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])
#ans:['cherry', 'orange', 'kiwi', 'melon', 'mango']
#This will return the items from index 2 to the end.
#Remember that index 0 is the first item, and index 2 is the third


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])
#ans:['apple', 'banana', 'cherry', 'orange']
#This will return the items from index 0 to index 4.
#Remember that index 0 is the first item, and index 4 is the fifth item
#Remember that the item in index 4 is NOT included


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])
#['orange', 'kiwi', 'melon']
#Negative indexing means starting from the end of the list.
#This example returns the items from index -4 (included) to index -1 (excluded)
#Remember that the last item has the index -1,


thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
#Yes, 'apple' is in the fruits list

#change list items

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)
#ans:['apple', 'blackcurrant', 'cherry']


thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)
#['apple', 'blackcurrant', 'watermelon', 'cherry']


thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)
#ans:['apple', 'watermelon']

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)
#ans:['apple', 'banana', 'watermelon', 'cherry']


#Add list items


thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
#['apple', 'banana', 'cherry', 'orange']


thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
#['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)
#['apple', 'orange', 'banana', 'cherry']


thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist) 
#['apple', 'banana', 'cherry', 'kiwi', 'orange']


#Remove list items


thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
#['apple', 'cherry']


thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)
#['apple', 'cherry', 'banana', 'kiwi']
#if there are more items it removes the first one


thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
#['apple', 'cherry']
#If you do not specify the index, the pop() method removes the last item


"""thislist = ["apple", "banana", "cherry"]
del thislist
print(thislist) #this will cause an error because you have succsesfully deleted "thislist".
"""

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist) #answer:[]


#Loop Lists

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
#apple
#banana
#cherry

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])
#apple
#banana
#cherry

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1
#apple
#banana
#cherry

thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]
#same answer


#List Comprehension

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
  if "a" in x:
    newlist.append(x)
print(newlist)
#['apple', 'banana', 'mango']

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)
#['apple', 'banana', 'mango']

#Sort lists

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
#['banana', 'kiwi', 'mango', 'orange', 'pineapple']


thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)
#[23, 50, 65, 82, 100]

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)
#['pineapple', 'orange', 'mango', 'kiwi', 'banana']


thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)
#[100, 82, 65, 50, 23]

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)
#['Kiwi', 'Orange', 'banana', 'cherry']

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)
#['banana', 'cherry', 'Kiwi', 'Orange']

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist) #['cherry', 'Kiwi', 'Orange', 'banana']


#Copy lists

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)
#or
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)
#or
thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)
#['apple', 'banana', 'cherry']

#Join lists

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)
#or
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
for x in list2:
  list1.append(x)
print(list1)
#or
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)
#['a', 'b', 'c', 1, 2, 3]

#PYTHON TUPLES

thistuple = ("apple", "banana", "cherry")
print(thistuple)
#('apple', 'banana', 'cherry')

thistuple = tuple(("apple", "banana", "cherry"))
print(len(thistuple))
#3

thistuple = ("apple",)
print(type(thistuple))
#NOT a tuple
thistuple = ("apple")
print(type(thistuple))
#<class 'tuple'>
#<class 'str'>


thistuple = tuple(("apple", "banana", "cherry"))
print(thistuple)
#('apple', 'banana', 'cherry')


#Access Tuple items

thistuple = ("apple", "banana", "cherry")
print(thistuple[1])
#banana

thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])
#cherry

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])
#('apple', 'banana', 'cherry', 'orange')

#Update Tuples

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)
#("apple", "kiwi", "cherry")


thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple)
#or
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple)
#('apple', 'banana', 'cherry', 'orange')


#Unpack Tuples

fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)
#apple
#banana
#cherry

#Loop Tuples

thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)
  #or
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])
#apple
#banana
#cherry

#Join Tuples

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)
#('a', 'b', 'c', 1, 2, 3)


fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)
#('apple', 'banana', 'cherry', 'apple', 'banana', 'cherry')


#PYTHON SETS

thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)#{'banana', 'cherry', 'apple'}
#Duplicate values will be ignored

thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)#{True, 2, 'banana', 'cherry', 'apple'}
#True and 1 is considered the same value

#Access set items

thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)
#banana
#apple
#cherry

thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)#True


#Add set items

thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)#{'banana', 'apple', 'orange', 'cherry'}

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)
#{'apple', 'mango', 'cherry', 'pineapple', 'banana', 'papaya'}

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)
#{'banana', 'cherry', 'apple', 'orange', 'kiwi'}

#Remove set items

thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)
#or
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)
#{'apple', 'cherry'}

"""thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset) #this will raise an error because the set no longer exists
"""

thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)#set()

thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x) #removed item
print(thisset) #the set after removal
#banana
#{'apple', 'cherry'}
#pop() will remove random item


#Loop sets

thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)
#apple
#cherry
#banana

#Join sets

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)
#or
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1 | set2
print(set3)
#{3, 'c', 'a', 2, 1, 'b'}


#PYTHON Dictionaries

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])
#Ford

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)#{'brand': 'Ford', 'model': 'Mustang', 'year': 2020}
#Dictionaries cannot have two items with the same key

#Access Items

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.get("model")
#or
x = thisdict["model"]
print(x)#Mustang


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.keys()
print(x)#dict_keys(['brand', 'model', 'year'])


car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.keys()
print(x) #before the change
car["color"] = "white"
print(x) #after the change
#dict_keys(['brand', 'model', 'year'])
#dict_keys(['brand', 'model', 'year', 'color'])


#Change Items

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})
print(thisdict)
#{'brand': 'Ford', 'model': 'Mustang', 'year': 2020}

#Add Items

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)
#or
thisdict.update({"color": "red"})
print(thisdict)
#{'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}

#Remove items

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)#{'brand': 'Ford', 'year': 1964}


thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)#{'brand': 'Ford', 'model': 'Mustang'}


thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)#{'brand': 'Ford', 'year': 1964}
#The del keyword can also delete the dictionary completely


thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)#{}


#

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(x)
  #or
for x in thisdict.keys():
  print(x)
#brand
#model
#year

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(thisdict[x])
  #or
for x in thisdict.values():
  print(x)
#Ford
#Mustang
#1964

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x, y in thisdict.items():
  print(x, y)
#brand Ford
#model Mustang
#year 1964


#Copy Dictionaries

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)
#or
mydict = dict(thisdict)
print(mydict)
#{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}


#Nested Dictionaries

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}
myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
print(myfamily)
#{'child1': {'name': 'Emil', 'year': 2004}, 'child2': {'name': 'Tobias', 'year': 2007}, 'child3': {'name': 'Linus', 'year': 2011}}


myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily)
#{'child1': {'name': 'Emil', 'year': 2004}, 'child2': {'name': 'Tobias', 'year': 2007}, 'child3': {'name': 'Linus', 'year': 2011}}


myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily["child2"]["name"])
#Tobias


#PYTHON IF ELSE

a = 33
b = 200
if b > a:
  print("b is greater than a")
#b is greater than a


a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
  #a is greater than b
  #The elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition
  
a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")
  #a is NOT greater than b


a = 2
b = 330
print("A") if a > b else print("B")#answer:B

#and Both conditions are true
#or at least one of the conditions is true


#PYTHON WHILE LOOPS

i = 1
while i < 6:
  print(i)
  i += 1 
  """answer:1 2 3 4 5(vertically)
  """

i = 1
while i < 6:
  print(i)
  if (i == 3):
    break
  i += 1  #answer:1 2 3
  
  
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)  #answer:1 2 4 5 6
# Note that number 3 is missing in the result


i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")
  #a:1 2 3 4 5 i is no longer than 6
  
  

#Python For Loops


for x in "ban":
  print(x) 
# b 
# a
# n


fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x) 
  if x == "banana":
    break 
  #answer: apple
  #        banana
  
  
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)    #apple
  
   
  
















