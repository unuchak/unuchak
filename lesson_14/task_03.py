def calc_mark_avg(marks):
    n = 0
    s = 0

    while n < len(marks):
        s += marks[n]
        n += 1

    return s / len(marks)


def main():
    marks = []

    size = int(input("Input numbers of students: "))

    while size > 0:
        mark = int(input("Input rating mark: "))
        marks.append(mark)
        size -= 1

    avg = calc_mark_avg(marks)
    avg = round(avg, 1)

    msg = f" Group average mark is {avg}"

    print(msg)


if __name__ == '__main__':
    main()
