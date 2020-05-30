MASK = "{:<5d}[{:<2d}] Bits"
last = None
for ss in range(0, 4097, 2):
    zlen = ss.bit_length()
    if zlen == last:
        continue
    last = zlen
    report = MASK.format(ss, zlen)
    print(report)
