#In this we are going to make a number guessing game
from random import random


lower_limit = int(input("Enter the lower limit: "))
upper_limit = int(input("Enter the upper limit: "))
range = (lower_limit, upper_limit)

x = random.randrange(range)
