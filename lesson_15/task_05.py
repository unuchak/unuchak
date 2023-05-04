def find_first_element(ls, value):
    index = 0

    while index < len(ls):
        if ls[index] == value:
            return index

        index += 1

    return None
