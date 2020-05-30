#!/usr/bin/env python3

# From Array
prefix = dict(((1,"DEBUG"), (2,"WARNING"), (3,"ERROR"), (4,"MESSAGE")))
# From List
prefix = dict([(1,"DEBUG"), (2,"WARNING"), (3,"ERROR"), (4,"MESSAGE")])
# From Dictionary
prefix = dict({(1,"DEBUG"), (2,"WARNING"), (3,"ERROR"), (4,"MESSAGE")})
prefix2 = dict(prefix)

def ShowChars(num, token):
        return "\t" + (token * (num + 4))
                        
def Show(ss, message):
        if(ss < 1):
                ss = 1
        if(ss > len(prefix)):
                ss = len(prefix)
        message = prefix[ss] + ": " + message
        xx = len(message)
        stars = ShowChars(xx, '*')
        print(stars)
        print("\t* " + message + " *")
        print(stars)

Show(999, "The is a MESSAGE")
Show(1, "Doh!")

for entry in prefix:
        print(entry, prefix[entry])
        

