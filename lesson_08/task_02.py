a = int(input("Input a: "))
b = int(input("Input b: "))
c = int(input("Input c: "))
d = int(input("Input d: "))

min_a_b = a if (a < b) else b
min_c_d = c if (c < d) else d

min_number = min_a_b if (min_a_b < min_c_d) else min_c_d

max_a_b = a if (a > b) else b
max_c_d = c if (c > d) else d

max_number = max_a_b if (max_a_b > max_c_d) else max_c_d

arithmetic_avg = (a + b + c + d) / 4

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
