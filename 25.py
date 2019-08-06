is will return True if two variables point to the same object, == if the objects referred to by the variables are equal.

>>> a = [1, 2, 3]
>>> b = a
>>> b is a
True
>>> b == a
True
>>> b = a[:] # Make a new copy of list `a` via the slice operator, and assign it to variable `b`
>>> b is a
False
>>> b == a
True