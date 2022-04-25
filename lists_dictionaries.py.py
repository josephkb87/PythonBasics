#We will cover lists in this#
course = "Python 101"
twitter = "@clydekingkid"

lst = ["String", 5, 3.14, ["A new item"], "King"]
# for item in lst:
#     print("The item is:", item)

#Part2
list1 = ["String", 1, 3.14, ["A new item"], "ClydeKingKid"]

# for item in lst:
#     print("The item is:", item)

print("The work on lists ends here for now")
print("We will look at dictionaries next")

#This looks at dictionaries basics#

name = "@clydekingkid"  #This is the teachers name
course = "Python 101"
twitter = ", @clydekingkid"

person = {
    "key": "value",
    "name": "ClydeKingKid",
    "twitter": "@clydekingkid",
}
# print(person['twitter'])

print(person)
person['instagram'] = "@life.is.code"
print(person)
del person['key']
print(person)

print("The work on dictionaries ends here for now")