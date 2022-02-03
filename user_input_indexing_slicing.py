# This looks at user input_and_indexing_slicing function

"""name = "@clydekingkid"  #This is the teachers name
course = "Python 101"
twitter = ", @clydekingkid"""

#We first input the details of our data entrant#
age = input("What is your age? ")

dog_years = int(age) * 7
name = input("What is your name? ")
print("Hello,", name)

print(name, "In dog years you are:",dog_years)

#We will use (one , two, three, four, five) as the list of elements#
input_string = input("Enter a list element separated by space ")
list  = input_string.split()

# lst = ['one', 'two', 'three', 'four', 'five']
# 0      1        2      3        4
print(list [::])
# b = True
# print(b[0])

course = "Python 101"
print(course[5])