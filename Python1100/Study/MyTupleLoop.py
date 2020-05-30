# File: MyTupleLoop.py

zList = ("Fred", 21, "Zelda", "Zoe", 54, 33)

print(type(zList))
for entry in zList:
    print(entry, "is", type(entry))


# TypeError: 'tuple' object does not support item assignment
zTuple = ("Fred", "Ralph", "Zelda", "Zoe")
print(type(zTuple))
for ss in range(len(zTuple)):
    zTuple[ss] = "Guest " + zTuple[ss]
    print(zTuple[ss])
