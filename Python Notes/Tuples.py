#Tuples
'''Tuples are similar to list but tuples are immutable and tuples are denoted with ()'''

'''
Tuples are ordered unchangeable and allows duplicate values'''

#create tuple
mytuple = ("python", "java", "javascript", "c++")
print(mytuple)

#another way to create my tuple
mytuple = tuple(("python", "java", "javascript", "c++"))
print(mytuple)

#accessing tuple items
mytuple = ("python", "java", "javascript", "c++")
print(mytuple[1])

#negative indexing
print(mytuple[-1])

#range of indexes
print(mytuple[2:4])

#range of negative indexes
print(mytuple[-4:-1])

#Tuples are immutable but if you want to update it you'll have to change it into list and again convert it into tuple
#changing items
mytuple = ("python", "java", "javascript", "c++")
x = list(mytuple)
x[1] = "fortran"

mytuple = tuple(x)
print(mytuple)

#Adding items
x = list(mytuple)
x.append("php")
mytuple = tuple(x)
print(mytuple)

#removing items
x = list(mytuple)
x.remove('php')
mytuple = tuple(x)
print(mytuple)

#del completely deletes the items
del mytuple
#print(mytuple) # this will raise an error as tuple has deleted completely.


#unpacking tuples
''' unpacking the tuples means extracting the vlaues back into variables'''
mytuple = ("python", "java", "javascript", "c++")
(lang1, lang2, lang3, lang4) = mytuple
print(lang1)

#joining tuples
'''joining the tuples simply means joining it and we use plus operator'''
tuple1 = ('a', 'b', 'c')
tuple2 = (1,2,3,4)
tuple3 = tuple1 + tuple2
print(tuple3)

#multiplying the tables
newtuple = mytuple*2
print(newtuple)

#tuple only allows two methods
#1. count
print(mytuple.count("python"))

#2. index()
print(tuple1.index(1))

