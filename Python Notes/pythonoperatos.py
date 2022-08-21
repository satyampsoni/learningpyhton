#Python operators
'''Operators are used to perform operations on variables and values.'''

#Python Arithmetic Operators
'''Arithmetic operators are used with numeric values to perform common mathematical operations:'''
x = 6
y = 2

print(x+y) #Addition

print(x-y) #substraction

print(x*y) #Multiplication

print(x/y) #Division

print(x%y) #Modulus

print(x**y) #Exponentiation

print(x//y) #Floor division

#Python Assignment Operators

x = 5 #is eqaul to
x += 3 # plus is equal to (it will increase the value by 3 everytime or x = x + 3)
x -= 3 # minus is equal to (it will decrease the value by 3 everytime or x = x - 3)
x *= 3 # asterisk is equal to (it will get multiplied by 3 evertime or x = x * 3)
x /= 3 # divison is equal to (it will divide it by 3 everytime or x = x/3)

#python comparison operators
'''comparison operators are used to compare two values'''

# equal operator (==)
x == y

# not equal (!=)

x != y

# greater than (>)

x>y

#less than (<)

x<y

# greater than or equal to
x >= y

#less than or equal to

x <= y


#logical operators

#and - Returns true if both the conditions are true 
#or - Returns true if either of the condition is true
#not - It reverses the result, If the answer is false and vice versa


#identity operator
'''when the objects are same but not equal identity operators are used to compare'''

#is operator - returns true if both the variables are same object
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)

# returns True because z is the same object as x

print(x is y)

# returns False because x is not the same object as y, even if they have the same content

print(x == y)

# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y

# is not - returns true if both the objects are not in same order

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is not z)

# returns False because z is the same object as x

print(x is not y)

# returns True because x is not the same object as y, even if they have the same content

print(x != y)

# to demonstrate the difference betweeen "is not" and "!=": this comparison returns False because x is equal to y

''' is like nft there can be copies of it but the one is assigned only have that true value for is'''