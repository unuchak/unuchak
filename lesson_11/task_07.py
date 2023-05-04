# :)
#:(
#:()
# :/\
# :/

from random import random, randrange

MOOD_NUMBER = 5
BED_MOOD = " :)"
HAPPY_MOOD = ":("
SHOUTED_MOOD = ":()"
NERVOUS_MOOD = ":/|"
NEUTRAL_MOOD = ":/"



def detect_mood():
    a = 1
    b = 5
    emotion = randrange(MOOD_NUMBER)

    if emotion == 1:
        msg = BED_MOOD

    elif emotion == 2:
        msg = HAPPY_MOOD
    elif emotion == 3:
        msg = SHOUTED_MOOD
    elif emotion == 4:
        msg = NERVOUS_MOOD
    else:
        msg = NEUTRAL_MOOD

    return msg


def main():
    mood = detect_mood()
    print(mood)


main()
