#Example2#
#Looping through Lists#
cats = ['Tomas', 'Snugly', 'Cute', 'Jasp', 'Cali']
queue = ["Judd", "Simon", "John"]
length = len(queue)

for i in range(0, length):
name = queue[i]
print("{} is at {}. position".format(name, i + 1))
#More Examples#
#Using the zip function with integers#
#Example2#
L1 = [1 , 2 , 3 , 4 , 5]
zip_L1 = zip ( L1 )
print(list(zip_L1))
# When the Iterables are of Different Lengths#
L2 = ['a' , 'b' , 'c' , 'd']
zip_L1L2 = zip ( L1 , L2 )
print ( list ( zip_L1L2 ) )
print("..........") # We will use this to separate our different outputs#