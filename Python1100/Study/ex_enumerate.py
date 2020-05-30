# File: ex_enumerate.py

# Pythonic Construct

for ss, ref in enumerate("nagy"):
    print(ss, ".)", ref)

print()

for ss, ref in enumerate("nagy", 9000):
    print(ss, ".)", ref)


