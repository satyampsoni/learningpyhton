#lambda function
#A lambda function can take any number of arguments, used as anonymus function
#syntax(lambda arguments : expression)

#returns the square of a 
x = lambda a : a*a
print(x(5))
print(x(6))

#returns argument a with argument b return the result
x = lambda a,b : a*b
print(x(5,6))
print(x(6,7))

y = lambda a,b,c : a+b+c
print(y(2,3,4))
print(y(7,8,4))

#using lamba in a function
def myfun(n):
    return lambda a: a*n

myfun(2)
