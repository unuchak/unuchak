ls = [45, 67, 345, 457, 6]

index = 0
while index < len(ls):
    print(ls[index], end=' ')

index += 1

index = len(ls) - 1

while index >= 0:
    print(ls[index], end=' ')
    index -= 1
