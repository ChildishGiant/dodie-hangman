import copy
import itertools

# Rules
secondBRule = True

firsts = []
lasts = []

with open("first.txt", "r") as file:
    firsts = file.read().splitlines()

with open("last.txt", "r") as file:
    lasts = file.read().splitlines()


combos = list(itertools.product(firsts, lasts))
toEdit = copy.deepcopy(combos)

with open("possibilities.txt", "w") as file:

    for n in range(0, len(combos)):

        combo = combos[n]

        if secondBRule and "B" in combo[0] + combo[1][0:3]+combo[1][4:]:
            file.write(combo[0] + " A " + combo[1] + "\n")
