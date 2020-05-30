#!/usr/bin/env python3

prefix = set()
prefix.add("Pig")
prefix.add("Cat")
prefix.add("Pig")
prefix.add("Dog")

for dat in prefix:
        print(dat)
        

prefix2 = set(("pig", "Mouse", "Pig", "Dog"))

print(prefix2.intersection(prefix))

print(prefix2.union(prefix))

prefix = frozenset()
prefix.add("Pig")


