#!/usr/bin/env python3
# File: MyBannerArrayTest.py

# Mission: Create a regression-testable
# banner capability.

prefix = ("DEBUG", "WARNING", "ERROR", "MESSAGE")

def ShowChars(num, token):
    return "\t" + (token * (num + 4))

def Show(ss, message):
    result = [] # New
    if(ss < 1):
        ss = 1
    if(ss > 4):
        ss = 4
    message = prefix[ss - 1] + ": " + message
    xx = len(message)
    stars = ShowChars(xx, '*')
    result.append(stars)
    result.append("\t* " + message + " *")
    result.append(stars)
    return result

def my_test_common(banner):
    assert(banner)
    assert(len(banner) == 3)

def my_test():
    '''
    >>> my_test()
    '''
    for ztype in range(len(prefix)):
        for msg in ('The is a MESSAGE', 'Doh!'):
            my_results = Show(ztype + 1, msg)
            my_test_common(my_results)
            mline = my_results[1]
            assert(mline.find(msg) != -1)
            assert(mline.find(prefix[ztype]) != -1)
    msg = "Lime"
    MAX = len(prefix) + 1
    for ztype in (-1, 0, MAX):
        my_results = Show(ztype + 1, msg)
        my_test_common(my_results)
        mline = my_results[1]
        assert(mline.find(msg) != -1)
        if ztype >= len(prefix):
            assert(mline.find(prefix[MAX-2]) != -1)
        else:
            assert(mline.find(prefix[0]) != -1)
    # print("Zoom!")
    

from doctest import testmod
testmod()


