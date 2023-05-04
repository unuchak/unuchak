from random import randrange

SIDE_COUNT = 2


def throw_coin(count):
    heads = 0
    counter = 0

    if count > 0:

        while counter < count:

            side = randrange(SIDE_COUNT)
            if side == 0:
                heads += 1

            count += 1

    return heads, count - heads


def main():
    count = int(input("Input count of throwing: "))
    heads, tails = throw_coin(count)

    msg = f" Count of heads is {heads}, count is {tails}"
    print(msg)


main()