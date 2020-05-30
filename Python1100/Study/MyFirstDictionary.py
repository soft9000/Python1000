# File: MyFirstDictionary.py

zList = {1:"Mr. Ed", 2:"Miss Daisy", 3:"Mr. T", 4:"Dr. Who"}
print(type(zList))
for ss, entry in enumerate(zList):
    print(ss, ".)", entry.__hash__())

