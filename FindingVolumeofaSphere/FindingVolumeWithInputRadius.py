import math
radius = input("Enter Radius: ")
print("Radius: " + str(radius))
r = float(radius)
def print_volume():
volume = 4.0/3.0 * math.pi * (r*r*r)
print("Volume: " + str(round(volume,2)))
print (print_volume)
type(print_volume)
print_volume()