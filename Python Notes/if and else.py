#if and else
"if and else are conditional statements, works according to conditions"

#if statement
'''if statement gets executed if and only if the condition is true'''
a = 5
b = 3
if a>b: #note after every colon there comes a indentation in the next line
    print("a is greater than b")

#elif
'''This gets executed if the condition is not satisfied, There can be any number of elif statements'''
a = 5
b = 3
if b>a:
    print("b is greater than a")
elif a==b:
    print('a is equal to b')
else:
    print("a is greater than b")

#shorthandif
#with the help of short hand if the if statement gets executed only in one line

if a>b : print("a>b")

#shorthand if and else
#with the help of short hand if and else statement gets executed in just one line
a = 8
b = 2
print(a) if a>b else print(b)

# if and 
#gets executed if both the conditions are true
a = 50
b = 3
c = 2
if a>b and c>b:
    print("both the conditions are true")
else:
    print("one of the conditions is true")

if a>b or c>b:
    print("at least one of the condition is true")

#Nestedif 
#if ke andar if

x = 41
if x>10:
    print("x is greater than 10")
    if x>20:
        print("x is greater than 20")
else:
    ("not greater than 20")

#pass statement
#pass statement is used when there is nothing to execute for if

if b>a:
    pass

