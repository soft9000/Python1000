#!/usr/bin/env python3
pest = {'p', 'e', 's', 't'}
rest = {'r', 'e', 's', 't'}
best = {'b', 'e', 's', 't', 'b'}

print(type(pest))

print("Normalized pest:\t", pest)
print("Normalized rest:\t", rest)
print("Normalized best:\t", best)

print("union:\t\t\t", pest | rest | best)
print("intersect:\t\t", pest & rest & best)
print("order diff3:\t\t", pest ^ rest ^ best)
print("pest - rest - best:\t", pest - rest - best)
print("best - pest - rest:\t", best - pest - rest)
print("rest - best - pest:\t", rest - best - pest)

print(type(pest - rest - best))


