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










