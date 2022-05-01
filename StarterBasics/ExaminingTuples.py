# Our basic example of a tuple#
# Example1#
tuple1 = ("apple" , "banana" , "cherry")
for x in tuple1 :
	print ( x )  # THis prints our tuple#

# Example2#
# Making two tuples #
months1 = ('January' , 'February' , 'March' , 'April' , 'May' , 'June')
b = ("RedRoses" , "WhiteRoses" , "BlueRoses" , "PinkRoses" , "YellowRoses" , "BlackRoses")

t1 = tuple ( months1 )
t2 = tuple ( months2 )
# Tuples are immutable
print ( "Tuple" , months1 )
print ( "Tuple" , months2 )
xy = zip ( b , months1 )
print ( xy )

# Using the zip function#
a = ("John" , "Charles" , "Mike")
months2 = ('July' , 'August' , 'September' , 'October' , 'November' , 'December')
x = zip ( a , months2 )
print ( tuple ( x ) )

# Using the enumerate function#
my_tuple = ("Audi" , "Benz" , "Chevrolet" , "Daimler" , "EnzoFerari")
for i in enumerate ( my_tuple ) :
	print ( i )

#Making a dictionary out of two lists using zip and updating the dictionary values#
#Example1#
fields = ['name', 'last_name', 'age', 'job']
values = ['Peter', 'Micheal', '35', 'Python Dev']
a_dict = dict(zip(fields, values))                   		# This zips the lists into one dictionary#
a_dict.update({'job':'Full Stack Guru'}) 			# This changes our job#
a_dict.update(name = 'John',last_name ='Doe', age = 45)  # This changes our name,last_name and age#
print('Original Dictionary is:', a_dict)
print ( 'The new and updated Dictionary is:', a_dict)
#Updating the dictionary entry using the update method#

dict2 = {'age': '25' }
a_dict.update(dict2)
print ('The new and upto date Dictionary is:', a_dict)