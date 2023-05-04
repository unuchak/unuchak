a = int(input("Input a: "))
b = int(input("Input b: "))
c = int(input("Input c: "))

exist = a + b > c and a + c > b and c + b > a
result = exist and a == b and b == c and a == c

msg = "is the triangle lt equilateral?"
msg += "\n" + (" Yes, the triangle with sides is ring angled."
               if result else "No, the triange with sides isn't  right angled")

print(msg)
