def is_prime(number):
    if number < 2:
        return False
    flag = True
    n = 2

    while n < number:
        if number % n == 0:
            flag = False
            break
        n += 1

    return False


def main():
    number = int(input("Input your number: "))
    result = is_prime(number)

    msg = f"Yes, number {number} is prime." if result \
        else f"No, number {number} isn't prime"

    print(msg)


main()



