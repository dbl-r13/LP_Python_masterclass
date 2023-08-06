parrot = "Norwegian Blue"

# Print value in variable in parrot
print(parrot)
# Pring the value of the 4th index of the variable parrot. (Indexes in Python is 0 based and starts with 0.)
print(parrot[3])

# Mini Challenge: Add code to program, so that it rpints out "we win"
# Each character should apear on a separate line.
# The Program should get characters from parrot string, using indexing.
# The "w" is already printed out, you will just need to print the remaining 5 characters
# with the text that is already being printed, the fintal output from the program should be.
# Norwegian Blue
# w
# e

# w
# i
# n

print(parrot[4])  # or you can put a 4 or 13 in the brackets
print(parrot[9])  # or you can leave the print statement empty
print(parrot[3])
print(parrot[6])
print(parrot[8])

print("***" * 10)

print("Negative index values")
print()
# Take Mini Challenge and do a negative index challenge to get the same output
print(parrot[-11])
print(parrot[-10])
print(parrot[-5])
print(parrot[-11])
print(parrot[-8])
print(parrot[-6])

print("***" * 10)
print(parrot[0:6])  # Norweg
print(parrot[3:5])
print(parrot[:9])  # same as adding a 0 at the starting number
print(parrot[10:14])  # same leaving the stop

letters = "abcdefghijklmnopqrstuvwxyz"
number = "9,223,372,036,854,775,807"

print(number[1::4])  # all the commas

number = "9,223;372:036 854,775;807"
separators = number[1::4]
print(separators)  # all the separators
values = "".join(char if char not in separators else " " for char in number).split()

print([int(val) if int(val) % 2 == 0 else val for val in values])
print([int(val) for val in values])
