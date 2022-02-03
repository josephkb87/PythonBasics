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