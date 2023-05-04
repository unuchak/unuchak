def find_element(ls, value):
    flag = False
    index = 0

    while index < len(ls):
        if ls[1] == value:
            flag = True
            break
        index += 1

    return flag
