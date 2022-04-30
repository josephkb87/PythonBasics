# Our basic example of a  dictionary#
# Example1#
d = {}

# Adding the key value pair
d[5] = "Five"
d[10] = "Ten"
print ( "Dictionary" , d )

# Removing key-value pair
del d[10]
print ( "Dictionary" , d )

# More Examples#
# Example1#
newdict = {1 : 'a' , 2 : 'b' , 3 : 'c' , 4 : 'd'}
for i , k in enumerate ( newdict ) :
	print ( i , k )

# Example2#
enuz = {0 : 1 , 1 : 2 , 2 : 3 , 4 : 4 , 5 : 5 , 6 : 6 , 7 : 7}
for i , j in enumerate ( enuz ) :
	print ( i , j )

# To enumerate both keys#
for i , (k , v) in enumerate ( newdict.items ( ) ) :
	print ( i , k , v )

# To enumerate over the index, key, and values of a dictionary#
# your for loop#
for index , (key , value) in enumerate ( newdict.items ( ) ) :
	print ( index , key , value )