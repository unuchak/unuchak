
input_number = int(input("Введите пятизначное число\n"))
if 10000 <= input_number <= 99999:

    a = input_number % 10
    input_number //= 10
    b = input_number % 10
    input_number //= 10
    c = input_number % 10
    input_number //= 10
    d = input_number % 10
    input_number //= 10
    i = input_number % 10
    input_number //= 10


    result = a * 10000 + b * 1000 + c * 100 + d * 10 + i


else:
    result = "ERROR"

print(result)