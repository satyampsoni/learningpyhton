#strings
''' strings are characters either surrounded with double or single quotation marks'''



s = "satyam"
print(s)
print(type(s))

s = 'satyam'
print(s)

#multiline strings
mls = """"Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""

#len function in string
#len function basically tells the length of string
print(len(s))
print(len(mls))

#string indexing
''' indexing in string allows to grab characters with help of its position value.
indexing are of two types forward indexing and reverse indexing.
forward indexing- indexing starts from 0 and ends at (l-1), reverse indexing- indexing starts from -1 and goes to -l.
Reverse indexing grabs characters from backwards'''


s = "satyam"
print(s[0])
print(s[1])
print(s[2])
print(s[3])
print(s[4])
print(s[5])

#reverse indexing
print(s[-1])
print(s[-2])
print(s[-3])
print(s[-4])
print(s[-5])
print(s[-6])

#stringslicing
#As the name suggests slicing means a slice of a string
# syntax: stringname[startindex : endindex]

s = "satyam"
print(s[0:3]) #the output is sat

#slice from start
print(s[:5])

#slice to end
print(s[4:])

#Negative slicing
print(s[-5:-2]) 

#Modifying the strings

''' Upper case - all the characters will turn uppercase. The upper method returns the string in uppercase.'''
s = "stringupper"
print(s.upper())

s = "STRINGLOWER"
print(s.lower())

#REMOVE EXTRA WHITE SPACE
s = " Hello Guys"
print(s)
print(s.strip()) #the strip method removes whitespace from the beginning or the end

#Replacing characters of string
'''The replace method replace one character with another'''
s = "Syring"
print(s.replace("y", 't'))

#split 
''' The split method returns a list when you
 use a seperated coloumn'''
s = "Hello , guys"
print(s.split(","))

#string concatenation
''' to combine string use the strings with plus operator'''

a = "Hi"
b = 'sam'
print (a + b) # this will print a string with no space

a =  "Hi"
b = "sam"
print(a + " " + b) #in order to add a space use "" with plus operators surrounding

#stirng formatting
'''we cannot add string and a number in python with plus method we have to use format method'''

age = 18
text = "Hi My name is Satyam and I am {} years old"
print(text.format(age))

'''so the format method takes the passed arguments like in the above example passed argument is age
 formats them into a string and places them in the string where the placeholders {} are present'''

age = 21
vote = 12
text = "The leader of age {} won by vote {}"
print(text.format(age, vote))

''' when there are multiple variables then each will be placed respectively'''

#Escape characters
''' Escape characters are used to place characters that string does not allow'''

#text = "Hi this is "satyam" "
''''This is not allowed in a string but in order to place it into  a string we need to use a escape characters'''
text = "Hi this is \"satyam\" "
print(text)

''' for more string methods we can use you can go to the link below and learn about it
 https://www.w3schools.com/python/python_strings_methods.asp'''

