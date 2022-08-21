#sets
#sets are used to store multiple items in one variable
'''sets are unorderd, unchangeable and unindexed'''

#creating a set
myset = {"satyam", 2 , 4 }
print(myset)

#set constructor
myset = set(("python", "java", "kotlin"))
print(myset)


#Acess set items 
'''if you want to acess set items you can't use idexing as it is unorderd'''

for x in myset:
    print(x)

#Adding items to the set
'''for adding items to the set'''
myset.add("x")
print(myset)

#adding two sets
set1 = {1,2,3,4}
set2 = {"a", "b", "c"}
#set3 = set1 + set2 this will raise an error
#print(set3)

set1.update(set2)
print(set1)

#or

set1.union(set2)
print(set1)
#Removing items from a set
'''1. .remove()
2. .discard()
3. .pop()
4. del'''

