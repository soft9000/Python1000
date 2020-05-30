#!/usr/bin/env python3
def ShowStars(num):
	return "\t*" + ("*" * (num + 3))
			
def Show(message):
	xx = len(message)
	stars = ShowStars(xx)
	print(stars)
	print("\t* " + message + " *")
	print(stars)

Show("The is a MESSAGE")

