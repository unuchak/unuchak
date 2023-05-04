import math

# number = 12.36
#
# print(int(number))
# print(math.trunc(number))
# print(math.floor())

number = float(input("Input your number: "))
number += 0.5 if number >= 0 else -0.5
number = int(number)
print(number)




