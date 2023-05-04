NUMBER_OF_STUDENT = 5


def calc_mark_avg(mark1, mark2, mark3, mark4, mark5):
    s = mark1
    s += mark2
    s += mark3
    s += mark4
    s += mark5

    return s / NUMBER_OF_STUDENT


def main():
    mark1 = int(input("Input rating mark1: "))
    mark2 = int(input("Input rating mark2: "))
    mark3 = int(input("Input rating mark3: "))
    mark4 = int(input("Input rating mark4: "))
    mark5 = int(input("Input rating mark5: "))

    avg = calc_mark_avg(mark1, mark2, mark3, mark4, mark5)
    avg = round(avg, 1)

    msg = f" Group average mark is {avg}"

    print(msg)


if __name__ == '__main__':
    main()
