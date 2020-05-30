#!/usr/bin/env python3

# Change tab to spaces:
def ShowChars(num, token):
	return (token * (num + 4))
			
def Show(message):
	xx = len(message)
	stars = ''
	if xx > 5:
		stars = ShowChars(xx, '$')
	else: 
		stars = ShowChars(xx, '*')
	print(stars)
	print("* " + message + " *")
	print(stars)

def test_show():
        '''
>>> Show("The is a MESSAGE")
$$$$$$$$$$$$$$$$$$$$
* The is a MESSAGE *
$$$$$$$$$$$$$$$$$$$$
>>> Show("Doh!")
********
* Doh! *
********
        '''
        return True

from doctest import testmod

testmod()






