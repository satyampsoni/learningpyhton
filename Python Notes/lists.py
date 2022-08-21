# lists
'''list are used to store multiple items in single variable'''
#creating a list
mylist = ["sting", 12, 12.5 ]

'''
some points about list
1. list items are ordered that is list items will have index values staring from 0, 
if you want to place any items it will be placed in the last of the list

2. list items are changeable i.e; lists are mutable it will allow changing, removing and replacing items in a list.

3. list items allow duplicates i.e; we can have multiple same items in a list'''

# list() constructor
''' It is also used to construct list by using list()'''

mylist = list(("satyam", 12, 12.5))
print(mylist)

#Accessing list items 
mylist = ["python", "java", "c++", "javascript"]

print (mylist[1]) #it will access the items from the list having index value at 1
print(mylist[-1]) # THis is known as reverse indexing it will access the items having index value -1

#slicing [a:b] where a and b are index positions
mylist = ["python", "java", "c++", "javascript"]
print(mylist[2:4]) #grab the items having indexes 2 and 3

print(mylist[1:3]) #grab the items having indexes 1 and 2

#Note: while accessing items the outer index is excluded always

#change the list items
'''In order the change the items refer to the index'''
mylist = ["python", "java", "c++", "javascript"]
mylist[-1] = "typescript"
print(mylist) #javascript will be replaced with typescript

#change a range of items 
mylist = ["python", "java", "c++", "javascript"]
mylist[1:3] = ["javascript", "c"]
print(mylist)

#Adding list to items
'''There are three ways in which we can add list items
1. append() - adds items to the end of the list
2.insert() - insert items to the list as specified index position
3.extend - to append elements from another list to the current list'''

mylist = ["python", "java", "c++", "javascript"]

mylist.append("php")
print(mylist)

mylist.insert(1, "SQL")
print(mylist)

mylist.extend(mylist)
print(mylist)

#Removing items from the list
''' There are various methods to remove items from a list
1. remove(item) - removes the specified items from a list
2. pop() - removes the specified index from a list
3. del - removes the specified index
4.clear() - clear the elements but the list still remains'''

#1. remove(item) - removes the specified items from a list
mylist = ['python', 'SQL', 'java', 'c++', 'javascript', 'php', 'python', 'SQL', 'java', 'c++', 'javascript', 'php']
mylist.remove('php')
print(mylist)

#pop() - removes the specified index from a list
mylist = ['python', 'SQL', 'java', 'c++', 'javascript', 'php', 'python', 'SQL', 'java', 'c++', 'javascript', 'php']
mylist.pop(2)
print(mylist)

#3. del - removes the specified index
mylist = ["python", "java", "c++", "javascript"]
del mylist[0]
print(mylist)

# 4.clear() - clear the elements but the list still remains'''
mylist = ['python', 'SQL', 'java', 'c++', 'javascript', 'php', 'python', 'SQL', 'java', 'c++', 'javascript', 'php']
mylist.clear()
print(mylist)

#list comprehension
#syntax - [expression for item in iterable if condition == True]

'''list comprehension is used when we want to create a new list based on the existing list'''
fruits = ["apple", "banana", "mango", "kiwi", "cherry"]

newlist = [x for x in fruits if "a" in x]
''' the above line of code will make a newlist of all the elements from fruits containing a in it'''
print(newlist)

newlist2 = [x for x in fruits if "e" in x]
''' the above line of code will make a newlist of all the elements from fruits containing a in it'''
print(newlist2)

newlist3 = [x for x in fruits if "i" in x]
print(newlist3)


#sorting the list 
''' sorting the list means sorting the items in alphabetically or numerically'''
#sort() funtion will be there 
mylist = ['python', 'SQL', 'java', 'c++', 'javascript', 'php', 'python', 'SQL', 'java', 'c++', 'javascript', 'php']
mylist.sort()
print(mylist)

#reversing a list 
''' If you want to reverse the order of a list use reverse function'''
mylist.reverse()
print(mylist)

#copying a list
''' we use copy() function to copy a list'''
mylist = ["This", "is", "machine", "learning"]
copylist = mylist.copy()
print(copylist)

#copying a list with list
thislist = ['this', 'is', 'programming']
mylist = list(thislist)
print(mylist)

#joining two list
list1 = ['a', 'b', 'c',]
list2 = [1,2,3,4]
list3 = list1 + list2
print(list3)

list1.extend(list2)
print(list1)

#for list methods here is the reference https://www.w3schools.com/python/python_lists_methods.asp

