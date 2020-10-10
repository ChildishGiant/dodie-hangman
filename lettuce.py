from nltk.corpus import wordnet as wn
import json
import copy
from AvsAn.AvsAn import AvsAn

printYeets = True
words = {}
results = {}

# Rules
positions = {"first": {2: "U"}, "last": {1: "P", 4: "B"}}
vowelRule = True
pluralRule = True
verbRule = True

yoteCount = {
    "vowelRule": 0,
    "pluralRule": 0,
    "verbRule": 0,
    "position": 0
}


def yeet(word, wordPos, reason):

    if printYeets:
        print("no", word, "-", reason)

    results[wordPos].remove(word)
    yoteCount[reason] += 1


with open("words.json") as file:

    words = json.load(file)

    results = copy.deepcopy(words)

for word in words["first"]:

    carryOn = True

    for pos in positions["first"]:
        if word[pos-1] != positions["first"][pos]:
            yeet(word, "first", "position")
            carryOn = False
            break

    if verbRule and carryOn:
        toYeet = True
        for tmp in wn.synsets(word):
            if tmp.pos()[0] == "v":
                toYeet = False
                break

        if toYeet:
            yeet(word, "first", "verbRule")


for word in words["last"]:

    if vowelRule and AvsAn.getInstance().query(word)["article"] == "an":
        yeet(word, "last", "vowelRule")
        continue

    if pluralRule and word[len(word)-1] == "S":
        yeet(word, "last", "pluralRule")
        continue

    for pos in positions["last"]:
        if word[pos-1] != positions["last"][pos]:
            yeet(word, "last", "position")


with open("first.txt", "w") as first:

    for word in results["first"]:
        first.writelines(word + "\n")


with open("last.txt", "w") as last:

    for word in results["last"]:
        last.writelines(word + "\n")

print("Yote:")
print(yoteCount)
