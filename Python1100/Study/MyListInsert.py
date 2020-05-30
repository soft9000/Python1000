# File: MyListInsert.py

# Rational insertion
zList = ["is", "a"]
zList.insert(0, "This")
zList.insert(3, "TEST!")
print(zList)

# Irrational insertion
zList = ["a"]
zList.insert(98, "little")  # 'at ss or end'
zList.insert(90, "lamb!")
zList.insert(-99, "had")    # 'make it 0'
zList.insert(-100, "Mary")
print(zList)


