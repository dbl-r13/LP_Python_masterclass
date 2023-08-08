string1 = "he's"
string2 = "probably"
string3 = "pining"
string4 = "for the"
string5 = "fjords"

print(string1 + string2 + string3 + string4 + string5)
print("Hello " * 5)

print("Hello " * (5 + 4))  # Hello 9 times
print("Hello " * 5 + "4")  # an error occurs if the 4 is an int and not a str.

today = "friday"
print("day" in today)  # True
print("fri" in today)  # True
print("thur" in today)  # False
print("parrot" in "fjords")  # False
