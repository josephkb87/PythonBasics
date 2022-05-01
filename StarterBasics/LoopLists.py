#Our basic example of a list#
#Input#
list1 = ["samsung", "nokia", "huawei"]
for x in list1:
  print(x)  									# This prints our list#

print("........") 								# We will use this to separate our different outputs#
#Using the zip function#
names = ['ChrisMartin', 'BobMarley', 'HusseinBolt']
ages = [24, 85, 38]
for name, age in zip(names, ages):
    print(name, age)  							#This print our outputs for ChrisMartin 24 # BobMarley 85 # HusseinBolt 38#
print("..........") 							# We will use this to separate our different outputs#

# Zipping two lists one with string and integer#
L3 = [1 , 2 , 3 , 4 , 5]
L4 = ['a','b','c','d','e']
zip_L3L4 = zip(L3,L4)
print(list(zip_L3L4))
print("..........") 							# We will use this to separate our different outputs#

#Using the enumerate function to add positions to the list items#
queue = ["Judd" , "Simon" , "John"]
for position , name in enumerate (queue):
print ( "{} is at {}. position".format ( name , position + 1 ) )
print("..........") 							# We will use this to separate our different outputs#

print('This marks the end of our conversation for now')
