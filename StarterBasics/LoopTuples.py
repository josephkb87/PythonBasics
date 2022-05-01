#Creating a Tuple# # Our Basic Example#
#Example1#
#Input#
tuple1 = ("apple", "banana", "cherry")
for x in tuple1:
print(x) # This prints our tuple#
print("........") 								# We will use this to separate our different outputs#
# Using the zip function to make two tuples#
##Input#
#Example1#
months1 = ('January', 'February', 'March', 'April', 'May', 'June')
b = ("RedRoses", "WhiteRoses", "BlueRoses", "PinkRoses","YellowRoses","BlackRoses")
xy = zip(b, months1)
print(tuple(xy))
print("........") 								# We will use this to separate our different outputs#
# Example2#
#Using the zip function to show that Tuples are immutable #
a = ("John", "Charles", "Mike")
months2 = ('July', 'August', 'September', 'October', 'November', 'December')
x = zip(a, months2)
print(tuple(x))
print("........") 								# We will use this to separate our different outputs#
#Using the enumerate function#
#Input#
mytuple = ("Audi", "Benz", "Chevrolet", "Daimler", "EnzoFerari")
for i in enumerate(mytuple):
print(i)
print("........") 								# We will use this to separate our different outputs#
print('This marks the end of our conversation for now')
