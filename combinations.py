import copy
import itertools
import json

printYeets = False

# Rules
secondBRule = True
oRule = True
allieFilterRule = False

firsts = []
lasts = []
allieFilter = []

with open("first.txt", "r") as file:
    firsts = file.read().splitlines()

with open("last.txt", "r") as file:
    lasts = file.read().splitlines()

with open("words.json", "r") as file:
    allieFilter = json.load(file)["allieFilter"]

combos = list(itertools.product(firsts, lasts))
toEdit = copy.deepcopy(combos)


def yeet(combo, reason):

    if printYeets:
        print("no", combo, "-", reason)

    toEdit.remove(combo)
    # yoteCount[reason] += 1


for n in range(0, len(combos)):

    combo = combos[n]

    if secondBRule and "B" not in combo[0] + combo[1][0:3]+combo[1][4:]:
        yeet(combo, "secondBRule")
        continue

    if oRule and "O" not in combo[0] + combo[1]:
        yeet(combo, "secondBRule")
        continue

    if allieFilterRule and (combo[0] not in allieFilter or combo[1] not in allieFilter):
        yeet(combo, "allieFilter")


with open("possibilities.txt", "w") as file:

    for combo in toEdit:
        file.writelines(combo[0] + " A " + combo[1] + "\n")
