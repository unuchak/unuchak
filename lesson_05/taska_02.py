number = int(input("Input your number: \n "))

a = number % 10
b = number // 10


result = (a % 2 == 0) and (b % 2 == 0)



#
#
# print(number % 2 == 0)
# print(number % 2 != 0)
print("Has", number, "all digits even?")
print("Answer", result )


