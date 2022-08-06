# Used to pass values from one function to another in a program, We look at their usage in a funtion to return objects to  the caller function.
# We look at how to return a single value like a number or string or a container object (dictionary, tuple or lst)

# Using the return function to find the sum of two NUmbers
import output as output


def sumofNumbers(Numb1, Numb2):
    result = Numb1+ Numb2
    return result

output = sumofNumbers(15, 30)
print("Sum of 15 and 30  is:", output)

#Output
#Sum of 15 and 30 is: 45

# Returning Container Objects
# Squaring the objects in a container and returning the value

def square(list2):
    newList = list2()
    for i in list2:
        newList.append(i * i)
        return newList

    input_list = [1,2,3,4,5,6]
    print("input list is:",  input_list)
    output = square(input_list)
    print("Output list is:", output)

    #Output
    #input list is: [1, 2, 3, 4, 5, 6]
    #output list is: [1, 4, 9,16, 25, 36]

    ## The yield Function
    # The yield function also used in a function to return values to the caller function
    # But it is exexcuted in the function and returns a generator object tothe caller.
    # The value in the generator object can be accessed using the next() function or a forloop

def square(list1):
    newList = list()
    for i in list1:
        newList.append(i * i)
    yield newList


input_list = [1, 2, 3, 4, 5, 6]
print("input list is:", input_list)
output = square(input_list)
print("Output from the generator is:", output)
print("Elements in the generator are:",next(output))

#Output
#input list is: [1, 2, 3, 4, 5, 6]
#Output from the generator is: <generator object square at 0x000002A260586D60>
