a = 12
b = 3

# Addition Opporator
print(a + b)  # 15
# Subtraction Opporator
print(a - b)  # 9
# Multiplication Opporator
print(a * b)  # 36
# Divison Opporator (will produce a float)
print(a / b)  # 4.0
# Integer Division Opporator (will produce a int)
print(a // b)  # 4 integer division, rounded down towards minus infinite
# Modulo Opporator
print(a % b)  # 0 modulo: the remainer after integer division

print("*" * 30)
# If 1 slash is used below, it will produce a TypeError
for i in range(1, (a // b) + 1):
    print(i)
# Below is the same as above, just more lines of code
# i = 1
# print(i)
# i = 2
# print(i)
# i = 3
# print(i)

# Doing PEMDAS from left to right gets us -35 which is the answer from the below statement
print(a + b / 3 - 4 * 12)
