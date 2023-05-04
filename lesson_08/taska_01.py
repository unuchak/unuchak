a = int(input("Input a: "))
b = int(input("Input b: "))
c = int(input("Input c: "))
d = int(input("Input d: "))

min_number = min(a, b, c, d)
max_number = max(a, b, c, d)
arithmetic_avg = sum((a, b, c, d)) / 4

multiply_values = a * b * c * d
n = 4
geometrical_avg = multiply_values ** (1 / n)

msg = f"""
min: {min_number}
max: {max_number}
arithmetic average: {arithmetic_avg}
geometrical average: {geometrical_avg}
"""

print(msg)