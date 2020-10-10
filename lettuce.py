from nltk.corpus import wordnet as wn
import json
from AvsAn.AvsAn import AvsAn

printYeets = False
words = {}

# Rules
positions = {"first": {2: "U"}, "last": {4: "B"}}
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

    del words[wordPos][words[wordPos].index(word)]
    yoteCount[reason] += 1


with open("words.json") as file:

    words = json.load(file)

for word in words["first"]:

    for pos in positions["first"]:
        if word[pos-1] != positions["first"][pos]:
            yeet(word, "first", "position")
            continue

    if verbRule:
        toYeet = True
        for tmp in wn.synsets(word):
            if tmp.name().split('.')[0] == word:
                if tmp.pos() == "v":
                    toYeet = False

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

    for word in words["first"]:
        first.writelines(word + "\n")


with open("last.txt", "w") as last:

    for word in words["last"]:
        last.writelines(word + "\n")

print("Yote:")
print(yoteCount)