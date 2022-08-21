#loops
'''there are two types of loops in python 
1. for loop
2. while loop'''

#1. while loop
#while loop gets executed as long as the conditon is true

'''i = 1 #initialisng the value
while i<8: #setting the condition
    print(i)'''
    
    #this will print infinte loop as i will always be less than we have no increasing condition and keep on printing 1


i = 1 #initialisng the value
while i<8: #setting the condition
    print(i)
    i +=1


#break statement
#the break statement breaks the loop even if the statement is true


i = 1 #initialisng the value
while i<8: #setting the condition
    print(i)
    if i == 7:
        break
    i +=1 

#continue statement
#continue statement breaks the current iteration and continue with the next

i = 0
while i<8:
    if i==3:
        continue
    print(i)
    i +=1



