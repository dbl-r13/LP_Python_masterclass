letters = "abcdefghijklmnopqrstuvwxyz"
backwards = letters[::-1]  # [::-1] = reverse
print(backwards)

# Challenge: Using letters string, add some code to create the following slices
# Create a slice that produces characters "qpo"
print(letters[16:13:-1])
# Slice the string to produce "edcba"
print(letters[4::-1])
# Slice the string to repoduce the last 8 characters in reverse order
print(letters[25:17:-1])  # Also could have used letters[:-9:-1]
