age_dragon = int(input("Input the dragon age: "))

total = 3

if age_dragon <= 100:
    total += total + age_dragon * 3

elif age_dragon <= 200:
    total += 300 + (age_dragon - 100) * 2

else:
    total += 300 + 200 + (age_dragon - 200) * 1

msg = f"Drakon has {total} heads"

print(total)
