# File: MyListDelete.py

# OKAY! Rational item removal
zList = ["This", "is", "a", "Test"]
zPop = zList.pop(0)
print("Popped:", zPop)
print("Result:", zList)

# ERROR! Irrational removal
zList = ['Mary', 'had', 'a', 'little', 'lamb!']
zList.pop(-100) # IndexError: pop index out of range
zList.pop(99)   # IndexError: pop index out of range
print(zList)




