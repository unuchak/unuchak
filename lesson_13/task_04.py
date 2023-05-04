# 12345643


def find_max_digit(number):
    number = abs(number)

    max_value = 0

    while number > 0:
        digit = number % 10

        if max_value < digit:
            max_value = digit

        if max_value == 9:
            break

        number //= 10

    return max_value


def main():
    number = int(input("int your number: "))
    max_value = find_max_digit(number)
