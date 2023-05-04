def pifagore_table(size):
    table_size = ""
    multy = 1
    for multy in range(1, size + 1):
        for item in range(1, size + 1):
            table_size += str(item * multy) + '\t'

        table_size += '\n'
        multy += 1

    return table_size


print(pifagore_table(9))
