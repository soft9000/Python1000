# File: MyHashCode.py

# Since Python 3.2.3
#import os
#print(os.environ['PYTHONHASHSEED'])
#print(os.environ)

# Changes EACH RUN!
print("a".__hash__())
print(hash("a"))

# Work Around:
import zlib
zBytes = bytes("a","utf8") # more later!
print("Classic:",
      zlib.crc32(zBytes) )

# Work Around:
import hashlib
zBytes = bytes("a","utf8") # more later!
print("hashlib:",
      hashlib.md5(zBytes).hexdigest() )

