def some(condition):
    if condition == 10:
        msg = "1"
    elif condition == 20:
        msg = "2"

    else:
        msg = "Error"

    return msg


print(some(10))
