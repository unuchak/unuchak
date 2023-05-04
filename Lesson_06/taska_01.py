a = int(input("Input a: "))
b = int(input("Input b: "))
c = int(input("Input c: "))

result = a + b > c and a + c > b and c + b > a

msg = "Does a triangle with given sides exist"
msg += "\nAnswer: " + str(result)
print(msg)
