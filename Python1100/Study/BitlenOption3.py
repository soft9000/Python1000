last = None
for ss in range(0, 4097, 2):
    zlen = ss.bit_length()
    if zlen == last:
        continue
    last = zlen
    report = f"{ss:<5} [{zlen:<2}] Bits"
    print(report)



