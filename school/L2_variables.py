# word = "Python"

# number = 42

# coefficient = 2.87

# fruits = ["apple", "mango", "grape"]

# ordinals = {1: "first", 2: "second", 3: "third"}

# class SomeCustomClass: pass
# instance = SomeCustomClass()

# # some types are string, integer, floating-point number, list, tuple, dictionary, custom object

# # also we don't specify the data type in python because the data type checking is done at runtime 
# # rather than compilation time


# # the variables don't have the data types but the objects being referenced by the variables do
# name = "Jane Doe"
# age = 19
# subjects = ["Math", "English", "Physics", "Chemistry"]

# print(type(name))
# # <class 'str'>
# print(type(age))
# # <class 'int'>
# print(type(subjects))
# # <class 'list'>


# # python expressions are simple statements that give you a return statement
# sum1 = 2 * 3.1416 * 10
# # 62.912
# print(sum1)
# sum2 = 2 * 3.1416 * 20
# # 125.824
# print(sum2)


# # setting counters can help track the frequency of a particular object, often given adefault value of 0 
# str_counter = 0

# for item in ("Alice", 30, "Programmer", None, True, "Department C"):
#     if isinstance(item, str):
#           str_counter += 1

# print(str_counter)
# # 3


# # accumulators can be used to add consecutive objects together
# numbers = [1, 2, 4, 6, 8, 10]
# total = 0

# for number in numbers:
#     total += number
    
# print(total)
# # 31


# # boolean flags can be used to alter the result of decisions in coditionals, while loops and boolean expressions
# toggle = True

# for _ in range(4):
#     if toggle:
#          print(f"✅ toggle is {toggle}")
#          print("Do something...")
#     else:
#          print(f"❌ toggle is {toggle}")
#          print("Do something else...")
#     toggle = not toggle

# # ✅ toggle is True
# # Do something...
# # ❌ toggle is False
# # Do something else...
# # ✅ toggle is True
# # Do something...
# # ❌ toggle is False
# # Do something else...


# # boolean functions
# def greet(name, verbose = False):
#     if verbose:
#         print(f"Welcome {name}, nice to meet you!")
#     else:
#         print(f"Welcome {name}!")
        
# greet("grate", verbose= True)
# greet("grate")


# # the sorted keyword uses boolean functions to reverse the order of the sort
# print(sorted([4, 2, 7, 5, 1, 6, 3]))
# # [1, 2, 3, 4, 5, 6, 7]

# print(sorted([4, 2, 7, 5, 1, 6, 3], reverse=True))
# # [7, 6, 5, 4, 3, 2, 1]


# # loop variables help process iterations in a for loop and sometimes a while loop by picking the value
# # of the current element ech time you go through the loop 
# colors = [
#      "red",
#     "orange",
#     "yellow",
#     "green",
#     "blue",
#     "indigo",
#     "violet"
# ]
# for color in colors:
#      print(color)

# ''' red
#     orange
#     yellow
#     green
#     blue
#     indigo
#     violet '''

# cars = [
#     "Toyota",
#     "Benz",
#     "Ford",
#     "Pontiac",
#     "BYD",
# ]

# for index, car in enumerate(cars):
#     index += 1
#     print(index, car)
    
# ''' 1 Toyota
#     2 Benz
#     3 Ford
#     4 Pontiac
#     5 BYD '''


# count = 5

# while count:
#     print(count)
#     count -= 1

# ''' 5
#     4
#     3
#     2
#     1 '''


# contacts = [
#      ("Linda", "111-2222-3333", "linda@example.com"),
#      ("Joe", "111-2222-3333", "joe@example.com"),
#      ("Lara", "111-2222-3333", "lara@example.com"),
#      ("David", "111-2222-3333", "david@example.com"),
#      ("Jane", "111-2222-3333", "jane@example.com"),
# ]

# for contact in contacts:
#      print(contact)

# ''' ('Linda', '111-2222-3333', 'linda@example.com')
# ('Joe', '111-2222-3333', 'joe@example.com')
# ('Lara', '111-2222-3333', 'lara@example.com')
# ('David', '111-2222-3333', 'david@example.com')
# ('Jane', '111-2222-3333', 'jane@example.com') '''

# for name, phone, email in contacts:
#      print(phone, name)

# ''' 111-2222-3333 Linda
# 111-2222-3333 Joe
# 111-2222-3333 Lara
# 111-2222-3333 David
# 111-2222-3333 Jane '''

# information = [
#      ("Charles", 18, "likes ball"),
#      ("Ye", 23, "likes green"),
#      ("Gavi", 18, "likes blue"),
#      ("Fred", 28, "likes red")
# ]

# for index, info in enumerate(information):
#      index +=1
#      print(index, info)

# for name, age, likes in information:
#      print(name, age)


# using module level variables restricts direct access to the non-public variable
# _timeout = 30

# def get_timeout():
#      print(_timeout)

# def set_timeout(seconds):
#      global _timeout
#      if seconds <= 0:
#           raise ValueError("timeout must be positive")
#      print(seconds)
     
# set_timeout(10)


# if you would like to use a keyword for naming a variable you'll need to follow it with an underscore
# class_ = "name"


# for some soft keywords like match it only matters in structural pattern matching
# import re

# text = "Some text containing a number: 123"
# match = re.search("123", text)

# if match:
#     print("Found a match 😃")
# else:
#     print("No match found 😔")


# for all the built-in names
# import builtins
# print(dir(builtins))


# here we're explicitly stating that our colors dictionary will be made up of string key and string values
# colors: dict[str, str] = {
#     "red": "#FF0000",
#     "green": "#00FF00",
#     "blue": "#0000FF",
#     "yellow": "#FFFF00",
#     "black": "#000000",
#     "white": "#FFFFFF",
# }

# colors: dict[str, tuple[int, int, int]] = {
#     "Red": (255, 0, 0),
#     "Green": (0, 255, 0),
#     "Blue": (0, 0, 255),
#     "Yellow": (255, 255, 0),
#     "Black": (0, 0, 0),
#     "White": (255, 255, 255),
# }


# tuple unpacking allows the creation of multiple variables to be used in an iterable of values
# person = ("Jane", 25, "Python Dev")
# name, age, job = person
# print(age)


# we can also use this to swap the values in variables
# fruits = ("apple", "banana", "orange", "guava")
# fruit_1, fruit_2, fruit_3, fruit_4 = fruits

# fruit_3, fruit_1 = fruit_2, fruit_4
# print(fruit_1)


# assignment expressions allow us to declare the result of conditionals and while loops into a name in one step
# line = input("Type some text: ")

# while line != "stop":
#     print(line)
#     line = input("Type some text: ")

# the cassigned expression in use 
# while (line := input("Type some text: ")) != "stop":
#     print(line)


# global variables are declared on the module level
# value = 42
# print(dir())
# ''' ['__annotations__',
#     '__builtins__',
#     '__cached__',
#     '__doc__',
#     '__file__',
#     '__loader__',
#     '__name__',
#     '__package__',
#     '__spec__',
#     'value'] '''


# local variables are declared in functions
# def function():
#     integer = 42
#     print(integer)

# function()

# integer # NameError: name 'integer' is not defined


# a general example illustrating global, local, non-local scope
# Global scope
global_variable = "global"

def outer_func():
    # Nonlocal scope
    nonlocal_variable = "nonlocal"
    def inner_func():
        # Local scope
        local_variable = "local"
        print(f"Hi from the '{local_variable}' scope!")
        print(f"Hi from the '{nonlocal_variable}' scope!")
        print(f"Hi from the '{global_variable}' scope!")
    inner_func()