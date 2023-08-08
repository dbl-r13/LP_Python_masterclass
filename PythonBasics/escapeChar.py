# New Line escape characters
splitString = "This string has been\nsplit over\nserveral\nlines"
print(splitString)
# Tabbed escape characters
tabbedString = "1\t2\t3\t4\t5"
print(tabbedString)
# Using escap characters for quotes.
print("The pet shop owner said \"No, no, 'e's uh ... he's resting\".")

print("""The pet shop owner said "No, no, 'e's uh,... he's resting". """)

anotherSplitStrings = """
This string has been
split over
serveral 
lines
"""
print(anotherSplitStrings)
# If you put a backslash (\) at the end of the variable in a triple quote it will ignore the new line break.

# How to escape backslash characters
print("C:\\Users\\username\\notes.txt")
# Using Raw Strings (r at front of Print statement)
print(r"C:\Users\username\notes.txt")
