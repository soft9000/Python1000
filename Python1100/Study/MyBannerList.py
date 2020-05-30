#!/usr/bin/env python3

prefix = ["DEBUG", "WARNING", "ERROR", "MESSAGE"]

def ShowChars(num, token):
        return "\t" + (token * (num + 4))
                        
def Show(ss, message):
        if(ss < 1):
                ss = 1
        if(ss > len(prefix)):
                ss = len(prefix)
        message = prefix[ss - 1] + ": " + message
        xx = len(message)
        stars = ShowChars(xx, '*')
        print(stars)
        print("\t* " + message + " *")
        print(stars)

def Append(zpre):
        prefix.append(zpre)

Append("TEST")
Show(999, "The is a MESSAGE")
Show(1, "Doh!")

for dat in prefix:
        print(dat)
        

