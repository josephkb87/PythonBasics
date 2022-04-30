def tryexcept(a,b):
a = (print("Enter the value of a:"))
a = int(input())
b = (print("Enter the value of b:"))
b = int(input())
print("a is:",a)
print("b is:",b)
if a > b:
try:
    c = a/b
except ZeroDivisionError:               #This is our exception Error#
    print("Cannot divide by zero")