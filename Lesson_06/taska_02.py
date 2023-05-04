a = int(input("Input a: "))
b = int(input("Input b: "))
c = int(input("Input c: "))

exist = a + b > c and a + c > b and c + b > a
result = exist and a == b or b == c or c == a

msg = "is the triangle lt isosceles?"
msg += "\nAnswer: " + str(result)
print(msg)
