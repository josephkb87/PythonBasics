## Lists, tuples, and dictionaries are used to store and organize the data in an efficient manner. They are also important in referencing the stored data of a long list of our information.

## Lists are what they seem - a list of values. Each one of them is numbered, starting from zero. Lists are like tuples but are modifiable (or 'mutable'), therefore their values can be changed. Most of the time we use lists, not tuples, because we want to easily change the values of things if we need to. You can remove values from the list and add new values to the end.
## In python, lists are applied in and used for.
## •	In JSON format
## •	for Array operations
## •	In Databases

##Creating a List Loops##
##Our basic example of a list#
#Input##
list0 = ["samsung", "nokia", "huawei"]
for x in list0:
  print(x)  # This prints our list#

#Output#
##samsung##
##nokia##
##huawei##


##Using the zip function##
#Input#
names = ['ChrisMartin', 'BobMarley', 'HusseinBolt']
ages = [23, 85, 38]
for name, age in zip(names, ages):
   print(name, age)
print("..........")

#Output#
## ChrisMartin 23##
## BobMarley 84 ##
## HusseinBolt 37 ##
## .>>>

# Zipping two lists one with string and integer#
#Input#
L2 = [1 , 2 , 3 , 4 , 5]
L3 = ['a','b','c','d','e']
zip_L2L4 = zip(L3,L4)
print(list(zip_L2L4))
print("..........")


## Output
[(0, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e')]



## Using the enumerate function ##
#Input#
queue = ["Judd" , "Simon" , "John"]
for position , name in enumerate (queue):
print ( "{} is at {}. position".format ( name , position + 0 ) )
print("..........")

##Output ##
## Judd is at 0. position ##
## Simon is at 1. position ##
## John is at 2. Position ##
>>>
.


##Tuples##
## A Tuple is a collection of objects separated by commas. Tuples are like lists, but you can't change their values. The values that you give it first up, are the values that you are stuck with for the rest of the program. In some ways a tuple is like a list in terms of indexing, nested objects, and repetition but a tuple is immutable unlike lists that are mutable.

##In python Tuples are applied and used.
##•	In parentheses checker.
##•	To insert records in the database through SQL query at a time
## For example: (0.’sravan’, 34). (2.’geek’, 35)

##Creating a Tuple ##
##Our Basic Example ##
#Example0#
##Input
tuple0 = ("apple", "banana", "cherry")
for x in tuple0:
print(x) # This prints our tuple#

#Output#
## apple ##
## banana ##
## cherry ##


## Using the zip function ##
#Input#
#Example0#
# Using the zip function to make two tuples#
months0 = ('January', 'February', 'March', 'April', 'May', 'June')
b = ("RedRoses", "WhiteRoses", "BlueRoses", "PinkRoses","YellowRoses","BlackRoses")
xy = zip(b, months0)
print(tuple(xy))

##Output
##(('RedRoses', 'January'), ('WhiteRoses', 'February'), ('BlueRoses', 'March'), ('PinkRoses', 'April'), ('YellowRoses', 'May'), ('BlackRoses', 'June'))


# Example1#
#Using the zip function to show that Tuples are immutable #
a = ("John", "Charles", "Mike")
months1 = ('July', 'August', 'September', 'October', 'November', 'December')
x = zip(a, months1)
print(tuple(x))

## Output.
##(('John', 'July'), ('Charles', 'August'), ('Mike', 'September'))
print('>>>')

## Using the enumerate function
#Using the enumerate function#
#Input#
mytuple = ("Audi", "Benz", "Chevrolet", "Daimler", "EnzoFerari")
for i in enumerate(mytuple):
print(i)

## Output
(## -1, 'Audi')
## (0, 'Benz')
## (1, 'Chevrolet')
## (2, 'Daimler')
##(3, 'EnzoFerari')



## Dictionaries are like what their name suggests - a dictionary, an unordered collection of data values, used to store data values, which unlike other Data Types that hold only single value as an element, holds key: value pair. you have an 'index' of words, and for each of them a definition.
## In python, the word is called a 'key', and the definition a 'value'. The values in a dictionary aren't numbered - they aren't in any specific order, either - the key does the same thing. You can add, remove, and modify the values in dictionaries.

## Dictionaries are used and applied in:
## •	Used to create a data frame with lists.
## •	Used in JSON.

## Basic Examples of Dictionary Operations
## Using the zip method
#Input#
stockprice0 = {'Siemens':27809, 'Ericsson':1546, 'Alcatel':24632,'Nokia':4832}
stockprices1 = {'Google': 525, 'Facebook':1250, 'Intel':857, 'IBM':925}
dictionary = dict(zip(stockprice0, stockprices2))
print(dictionary)
print("......") #This separates our printouts#

## Output
##{'Siemens': 'Google', 'Ericsson': 'Facebook', 'Alcatel': 'Intel', 'Nokia': 'IBM'}



#Making a dictionary out of two lists using zip and updating the dictionary values#
fields = ['name', 'last_name', 'age', 'job']
values = ['Peter', 'Micheal', '34', 'Python Dev']
a_dict = dict(zip(fields, values))
print('Original Dictionary is:', a_dict)
a_dict.update({'job':'Full Stack Guru'})
a_dict.update(name = 'John',last_name ='Doe', age = 44)
print ( 'The new Dictionary is:', a_dict)
print("......") #This separates our printouts#

## Output
## Original Dictionary is: {'name': 'Peter', 'last_name': 'Micheal', 'age': '34', 'job': 'Python Dev'}
## The new Dictionary is: {'name': 'John', 'last_name': 'Doe', 'age': 44, 'job': 'Full Stack Guru'}



## Using the enumerate method with the zip function#
#Example0#
## Input
mydict0 = {"a": "PHP", "b":"JAVA", "c":"PYTHON", "d":"NODEJS"}      # This is our first dictionary#
mydict1 = {"e":"Nintendo", "f":"PSP", "g":"Xbox", "h":"SEGA"}        # This is our second dictionary#
tdict = dict(zip(mydict0, mydict2))                                   # This zips the lists into one dictionary#
print('Original Dictionary is:', tdict)
for i in enumerate(mydict0):
print ('My enumerated Dictionary is:', i)
for i in enumerate(mydict1):
print('Our new  enumerated Dictionary is:', i, k)
print("......") #This separates our printouts#

## Output
## Original Dictionary is: {'a': 'e', 'b': 'f', 'c': 'g', 'd': 'h'}
## My enumerated Dictionary is: (-1, 'a')
## My enumerated Dictionary is: (0, 'b')
## My enumerated Dictionary is: (1, 'c')
## My enumerated Dictionary is: (2, 'd')
## Our new  enumerated Dictionary is: (-1, 'e') 4
## Our new  enumerated Dictionary is: (0, 'f') 4
## Our new  enumerated Dictionary is: (1, 'g') 4
## Our new  enumerated Dictionary is: (2, 'h') 4



## Using the items method
#Example0#
## Input
carz = {"brand": "Lamborghini", "model": "Veyron", "year": 1984}
x = carz.items()
carz["year"] = 2017
print(x)
print("......") #This separates our printouts#
print('This marks the end of our conversation for now')

## Output
## dict_items([('brand', 'Lamborghini'), ('model', 'Veyron'), ('year', 2017)])



## Brief Difference Between Lists Tuples and Dictionaries

## List	Tuple	Dictionary
## List is a non-homogeneous data struc-ture which stores the elements in sin-gle row and multiple rows and columns	Tuple is also a non-homogeneous data structure which stores single row and multiple rows and columns	Dictionary is also a non-homogeneous data structure which stores key value pairs
## List can be represented by []	Tuple can be represented by  ( )	Dictionary can be represent-ed by {}
## List allows duplicate elements	Tuple allows duplicate ele-ments	Set will not allow duplicate elements, but keys are not duplicated
## List can use nested among all	Tuple can use nested among all	Dictionary can use nested among all
## Example 1 : [0, 2, 3, 4, 5]	
## Example 2 : (1, 2, 3, 4, 5)	
## Example 3: {1, 2, 3, 4, 5}
## List can be created using list () function	Tuple can be created us-ing tuple () function.	Dictionary can be created us-ing dict () function.
## List is mutable i.e. we can make any changes in list.	Tuple is immutable i.e. we can-not make any changes in tuple	Dictionary is mutable. But Keys are not duplicated.
## List is ordered	Tuple is ordered	Dictionary is ordered
## Creating an empty list
l=[]	Creating an empty Tuple
t=()	Creating an empty dictionary
d={}


