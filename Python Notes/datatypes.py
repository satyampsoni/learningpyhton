# Data types in Python
''' Data types are used to state the type of the data in python'''

#type1 = int (stands for integer)
x = 5
print(type(x))

#type2 = float (It is a number containing decimals)

y = 2.3
print(type(y))

#type3 = complex (It is used to denote complex numbers)

z = 3j + 2
print(type(z))

''' In python iota is denoted with j not with i as due to convention'''

#type4 = str (It is used to store string)

a = "satyam"
print(type(a))

# type5 = list (It is used to store multiple data types)

li = ['satyam', 16, 0.5, 3j+2, ]
print(type(li))

#type6 = tuple (It is also used to store multiple data types but not repeatable)

tup = ("satyam", 15, 7.9)
print(type(tup))

#type6 = dict (It is used to denote dictionary a key value pair)
dictionary = {'key1' : 'value1' , 'key2' : 'value2'}
print(type(dictionary))

#type7 = set { It is used to denote set of numbers}

s = {1,2,3,4,5}
print(type(s))

#type8 = bool (It is used to denote booleans)

t = True # T should be capitalised
f = False # F should be capitalised

print(type(t))
print(type(f))

#type 9 = None (It is used to denote noneType)
n = None
print(type(n))