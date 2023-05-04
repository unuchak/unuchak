# Напишите программу, которая считывает целое число и выводит соответствующую ему римскую цифру. Если число находится вне диапазона 1-10,
# то программа должна вывести текст «ошибка».
# В таблице приведены римские цифры для чисел от 1 до 10.
# Число 	Римская цифра
# 1 	I
# 2 	II
# 3 	III
# 4 	IV
# 5 	V
# 6 	VI
# 7 	VII
# 8 	VIII
# 9 	IX
# 10 	X

def convert(number):
    if number < 1 or number > 10:
        return "ERROR. Number should be between 1 and 10."

    msg = "X"

    if number <= 3:
        msg = "I" * number

    elif number == 4:
        msg = "IV"

    elif number <= 8:
        msg = "V" + "I" * (number - 5)

    elif number == 9:
        msg = "IX"

    return msg


def main():
    number = int(input("Input number: "))
    print(convert(number))


#main()

def testing():
    result = "1---> I: " + str(convert(1) == "I")
    result += "\n2---> II : " + str(convert(2) == "II")
    result += "\n3---> III: " + str(convert(3) == "III")
    result += "\n4---> IV: " + str(convert(4) == "IV")
    result += "\n5---> V: " + str(convert(5) == "V")
    result += "\n6---> VI: " + str(convert(6) == "VI")
    result += "\n7---> VII: " + str(convert(7) == "VII")
    result += "\n8---> VIII: " + str(convert(8) == "VIII")
    result += "\n9---> IX: " + str(convert(9) == "IX")
    result += "\n10---> X: " + str(convert(10) == "X")

    result += "\n 0--> Error:" + str(convert(0) == "Error. Number should be between 1 and 10.")
    result += "\n 100 --> Error:" + str(convert(100) == "Error. Number should be between 1 and 10.")

    print(result)


testing()

