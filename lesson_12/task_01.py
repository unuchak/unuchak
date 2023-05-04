from random import randrange

SIDE_COUNT = 2


def throw_coin(count):
    heads = 0
    tails = 0

    if count > 0:

        while count > 0:

            side = randrange(SIDE_COUNT)
            if side == 0:
                heads += 1
            else:
                tails += 1

            count -= 1

    return heads, tails


def main():
    count = int(input("Input count of throwing: "))
    heads, tails = throw_coin(count)

    msg = f" Count of heads is {heads}, count is {tails}"
    print(msg)


def test_heads():
    count = 10
    heads, tails = throw_coin(count)
    return heads > 0


def test_tails():
    count = 10
    heads, tails = throw_coin(count)
    return tails > 0


def test_invalid_data():
    count = -5
    heads, tails = throw_coin(count)
    return heads == 0 and tails == 0


def test_suite():
    msg = "test_heads - " + str(test_heads())
    msg += "\ntest_tails - " + str(test_tails())
    msg += "\ntest_invalid_data - " + str(test_invalid_data())

    print(msg)


test_suite()
