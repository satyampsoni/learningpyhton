#for loops
#for loops is used to iterate over a sequence
lang = ["java", "python", "c++", "c", "php"]
for x in lang:
    print(x)

#break statement
for x in lang:
    print(x)
    if lang == "python":
        break

#continue
for x in lang:
    if x == "python":
        continue
    print(x)

#range
for x in range(6):
    print(x)

for x in range(2,6):
    print(x)

for x in range (2,10,2):
    print(x)

#else
for x in range (6):
    print(x)
else:
    print("finally finished")

#nestedloops
fruits= ["apple", "cherry", "mango"]
color= ["red", "green", "yellow"]
for i in fruits:
    for j in color:
        print(i,j)

#pass 
for x in [0,1,2]:
    pass