import random

wantedInt = int(input("Enter a number from 1 to 6"))


row1 = ["O", "O", "O"]
row2 = ["O", "O", "O"]
row3 = ["O", "O", "O"]

def peter(randInt):

    if randInt == 1:
        row1 = ["O", "O", "O"]
        row2 = ["O", "X", "O"]
        row3 = ["O", "O", "O"]
    if randInt == 2:
        row1 = ["X", "O", "O"]
        row2 = ["O", "O", "O"]
        row3 = ["O", "O", "X"]
    if randInt == 3:
        row1 = ["X", "O", "O"]
        row2 = ["O", "X", "O"]
        row3 = ["O", "O", "X"]
    if randInt == 4:
        row1 = ["X", "O", "X"]
        row2 = ["O", "O", "O"]
        row3 = ["X", "O", "X"]
    if randInt == 5:
        row1 = ["X", "O", "X"]
        row2 = ["O", "X", "O"]
        row3 = ["X", "O", "X"]
    if randInt == 6:
        row1 = ["X", "O", "X"]
        row2 = ["X", "O", "X"]
        row3 = ["X", "O", "X"]

    return (row1, row2, row3)


while True:
    RandomInt = random.randrange(1, 7)
    for row in peter(RandomInt):
        print(row)
    print("------------------------------------")
    if RandomInt == wantedInt:
        break
