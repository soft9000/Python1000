#!/usr/bin/env python3
cat = {'c','a','t'}
car = set()
car.add('c');car.add('a');car.add('r')

print(type(cat))
print("Normalized cat:", cat)
print("Normalized car:", car)

# set() = unique set, 'venn style
print("cat | car:", cat | car) # union
print("cat & car:", cat & car) # intersect
print("cat - car:", cat - car) # 'remove common car from cat'
print("cat ^ car:", cat ^ car) # order dif

print(type(cat - car))


