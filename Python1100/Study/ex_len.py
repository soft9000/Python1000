# File: ex_len.py

zstring = "123,456,789"
print(len(zstring))

print()

ss = 0
for ch in zstring:
    print(ss, "=", ch)
    ss += 1

