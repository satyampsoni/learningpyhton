#functions
#functions are block of code which only runs when it is called

#creating a function
def my_func():
    print("my first function")

my_func() #calling a function

#arguments - information are passed into functions with the help of arguments
#you can pass as many arguments as you want seperated with comma

def my_func(fname, rollno):
    print(fname , rollno)

my_func("satyam", 2)

#if you don't know how many arguments can be passed use keyword(*)
def my_func(*kids):
    print("the smartes child is " + kids[1])

my_func("satyam", "shivam")

#keyword arguments - if you don't know how many arguments should be passed into it
def my_func(**kwargs):
    print("His last name is" + kwargs["lname"])

my_func(name = "satyam", lname = " soni")

#default parameter value
def my_func (country = "India"):
    print("I am from " + country)
my_func()
my_func("America")
my_func("china")
