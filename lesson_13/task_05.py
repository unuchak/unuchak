def is_prime(number):
    if number < 2:
        return False

    n = 2

    while n < number:
        if number % n == 0:
            return False
        n += 1

    return True


def main():
    number = int(input("Input your number: "))
    result = is_prime(number)

    msg = f"Yes, number {number} is prime." if result \
        else f"No, number {number} isn't prime"

    print(msg)


main()
