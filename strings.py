# Double Quotes
print("Today is a good day to learn python")
# Single Quotes
print("Python is fun")
# Mixed starting with Double Quotes
print("Python's string are easy to use")
# Mixed starting with Single Quotes
print('we can even include "quotes" in strings')
# String Concatination
print("Hello" + " world")

# Variables
greeting = "Hello"
name = "Ryan"

# Below is how you get user input
# name = input("Please enter your name ")

# if we want a space we can add that too
print(greeting + " " + name)
print(greeting, name)

age = 24
print(age)

# How to show what class type an integer is.
print(type(greeting))
print(type(age))

# Reassigning age and testing what the type is.
age_in_words = "2 years"

# Will produce a TypeError
# print(name + " is " + age + " old")

# Below code will not error out.
print(name + " is " + age_in_words + " old")
print(type(age))
