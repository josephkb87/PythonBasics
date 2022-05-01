#Using the zip method##Adding two dictionaries out of two lists using zip together#
#Input#
stockprice1 = {'Siemens':27809, 'Ericsson':1546, 'Alcatel':24632,'Nokia':4832}
stockprices2 = {'Google': 525, 'Facebook':1250, 'Intel':857, 'IBM':925}
dictionary = dict(zip(stockprice1, stockprices2))
print(dictionary)
print("......") #This separates our printouts#

#Making a dictionary out of two lists using zip and updating the dictionary values#

a_dict = dict(zip(fields, values))                          # This zips the lists into one dictionary#
print('Original Dictionary is:', a_dict)                    # This prints our dictionary#
a_dict.update({'job':'Full Stack Guru'}) 			       # This the job dictionary entry using the update method#
a_dict.update(name = 'John',last_name ='Doe', age = 45)  # This changes our name,last_name and age#
print ( 'The new Dictionary is:', a_dict)
print("......") #This separates our printouts#

#using the enumerate method with the zip function#
#Example1#
mydict1 = {"a": "PHP", "b":"JAVA", "c":"PYTHON", "d":"NODEJS"}      # This is our first dictionary#
mydict2 = {"e":"Nintendo", "f":"PSP", "g":"Xbox", "h":"SEGA"}        # This is our second dictionary#
tdict = dict ( zip ( mydict1 , mydict2 ) )  # This zips the lists into one dictionary#

for i ,k in enumerate(mydict1):
print ('My enumerated Dictionary is:', i)
for i in enumerate(mydict2):
print('Our new  enumerated Dictionary is:', i, k)
print("......") #This separates our printouts#

#Using the items method#
#Example1#
carz = {"brand": "Lamborghini", "model": "Veyron", "year": 1985}
x = carz.items()
carz["year"] = 2018
print(x)
print("......") #This separates our printouts#
print('This marks the end of our conversation for now')
