# File: MySetOrDictionary.py


ss = 0;
zList = {"Mr. Ed", "Miss Daisy", "Mr. T", "Dr. Who"}
print(type(zList))
for entry in zList:
    ss += 1
    print(ss, ".)", entry.__hash__())

ss = 0;
zList = {"Miss Daisy", "Mr. T", "Dr. Who", "Mr. Ed"}
print(type(zList))
for entry in zList:
    ss += 1
    print(ss, ".)", entry.__hash__()) # no change!

ss = 0;
zList = {1:"Mr. Ed", 2:"Miss Daisy", 3:"Mr. T", 4:"Dr. Who"}
print(type(zList))
for entry in zList:
    ss += 1
    print(ss, ".)", entry.__hash__())

#spam = dict(1="Mr. Ed", 2="Miss Daisy", 3="Mr. T", 4="Dr. Who")
#zList = dict(spam)

# Any iterable will do
print(sorted(("Mr. Ed", "Miss Daisy", \
              "Mr. T", "Dr. Who"))) # Tuple
print(sorted(["Mr. Ed", "Miss Daisy", \
              "Mr. T", "Dr. Who"])) # List
print(sorted({"Mr. Ed", "Miss Daisy", \
              "Mr. T", "Dr. Who"})) # Set
print(sorted({1:"Mr. Ed", 2:"Miss Daisy", \
              3:"Mr. T", 4:"Dr. Who"})) # Dict (keys)

print(type({}))
print(type({"Mr. Ed", "Miss Daisy", \
              "Mr. T", "Dr. Who"}))
print(type({1:"Mr. Ed", 2:"Miss Daisy", \
            3:"Mr. T", 4:"Dr. Who"}))



