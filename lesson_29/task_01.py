from human import Human
from manager import Manager
from human_creator import HumanCreator

ls = HumanCreator.create()
for human in ls:
    print(human)

adult = Manager.count_adult(ls)
underage = Manager.count_underage(ls)
print(f"Adult - {adult}")
print(f"Underage - {underage}")

# h1 = Human()
# print(h1)
#
# h2 = Human("ALEX", 22)
# print(h2)
# print(h2.name)
