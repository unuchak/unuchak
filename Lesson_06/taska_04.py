a = int(input("Input a: "))
b = int(input("Input b: "))
c = int(input("Input c: "))

exist = a + b > c and a + c > b and c + b > a
result = exist and a**2 + b**2 == c ** 2 or b**2 + c**2 == a**2 or a**2 + c**2 == b**2

msg = "is lt a right triangle?"
msg += "\nAnswer: " + str(result)

print(msg)
