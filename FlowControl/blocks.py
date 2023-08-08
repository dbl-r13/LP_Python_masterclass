# For Loop that goes through from 1 not including 13 and give answers of what that number is squared and cubed.
for i in range(1, 13):
    print("No. {} squared is {} and cubed is {:4}".format(i, i**2, i**3))
    print("*" * 80)

# Creates an variable from input from user
name = input("Please enter your name: ")
# Creates an integer variable from input from user
age = int(input("How old are you, {0}?\n".format(name)))
print(age)

# Creates a code block with logic based on age that the user inputs
if age >= 18:
    print("You are old enough to vote")
    print("Plase put an X in the box")
else:
    print("Please come back in {0} years".format(18 - age))

# Below is the reverse Logic of what is above.
if age < 18:
    print("Please come back in {0} years".format(18 - age))
elif age == 900:
    print("Sorry, Yoda, you die in Return of the Jedi")
else:
    print("You are old enough to vote")
    print("Plase put an X in the box")
