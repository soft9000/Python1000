#!/usr/bin/env python3

prefix = ("DEBUG", "WARNING", "ERROR", "MESSAGE")

def ShowChars(num, token):
        return "\t" + (token * (num + 4))
                        
def Show(ss, message):
        if(ss < 1):
                ss = 1
        if(ss > 4):
                ss = 4
        message = prefix[ss - 1] + ": " + message
        xx = len(message)
        stars = ShowChars(xx, '*')
        print(stars)
        print("\t* " + message + " *")
        print(stars)

Show(4, "The is a MESSAGE")
Show(1, "Doh!")

