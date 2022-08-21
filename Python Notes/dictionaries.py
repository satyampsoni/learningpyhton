#Dicitionary
'''Dictionaries are used to store data values in key:value pairs'''
'''ictionaries are used to store data values in key:value pairs'''

#creating a dictionary
thisdict = {
    "python": 1991,
    "java": 1995,
    "c": 1972,
}

'''Dictionaries are orderd changeable and does not allow duplicates.'''
print(thisdict["python"])

#Acessing items from a dictionary
'''items form dictionary can be acessed by putting key values in square brackets'''

x = thisdict["java"]
print(x)

#we can also use get method to acess items from dictionary
x = thisdict.get("c")

#we can also key method to acess items from dictionary
x = thisdict.keys()

#change items in dictionary
#changing items from key

thisdict = {
    "python": 1991,
    "java": 1995,
    "c": 1972,
}

thisdict ["python"] = 1992

print(thisdict)

#using update method
thisdict.update({"HTML": 1995})
print(thisdict)

#ADDING ITEMS IN A DICTIONARY
thisdict["computerscience"] = 1947

#deleting items from a dictionary
#pop() is used to del specified key item
thisdict.pop("python")
print(thisdict)

#popitem() is used to remove the last inserted item
thisdict.popitem()
print(thisdict)


#copying a dictionary
'''There are two ways to copy a dictonary
1. copy()
2. dict()'''
mydict = thisdict.copy()
print(mydict)

#dict() method
thisdict = {
    "python": 1991,
    "java": 1995,
    "c": 1972,
}
mydict2 = dict(thisdict)
print(mydict2)


#nested dictionary
child1 = {"name": "x",
"year": 2001}

child2 = {
    "name": "y",
    "year": 2002
}
child3 = {
    "name": "z",
    "year": 2003
}

myfamily = {
    "child1": child1,
    "child2": child2,
    "child3": child3
}

print(myfamily)

#for more dictionary methods https://www.w3schools.com/python/python_dictionaries_methods.asp
