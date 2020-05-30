# File: MyListDelta.py

zList = ["Fred", "Ralph", "Zelda", "Zoe"]

# Lists are mutable
print(type(zList))
for ss in range(len(zList)):
    zList[ss] = "Guest " + zList[ss]
    print(zList[ss])

# TypeError: 'tuple' object does not support item assignment
zTuple = ("Fred", "Ralph", "Zelda", "Zoe")
print(type(zTuple))
for ss in range(len(zTuple)):
    zTuple[ss] = "Guest " + zTuple[ss]
    print(zTuple[ss])

