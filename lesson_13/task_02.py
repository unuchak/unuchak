def calc_factorial(number):
    if number < 0:
        return "Error! User data was invalid."
    factorial = 1
    n = 2

    while n <= number:
        factorial *= n
        n += 1

    return factorial


def main():
    numbers = int(input("Input your number: "))
    factorial = calc_factorial(numbers)
    msg = f"{numbers}! = {factorial}"
    print(msg)


if __name__ == "__main__":
    main()


def testing():
    msg = "calc_factorial(0) == 1 -" + str(calc_factorial(0) == 1)
    msg += "\ncalc_factorial(1) == 1 -" + str(calc_factorial(1) == 1)
    msg += "\ncalc_factorial(2) == 2 -" + str(calc_factorial(2) == 2)
    msg += "\ncalc_factorial(5) == 120 -" + str(calc_factorial(5) == 120)
    msg += "\ncalc_factorial(7) == 5040 -" + str(calc_factorial(7) == 5040)
    msg += "\ncalc_factorial(-1) == Error -" + str(calc_factorial(-1) == "Error")
    msg += "\ncalc_factorial(-10) == Error -" + str(calc_factorial(-10) == "Error")



