In [20]: def foo(target=[]):
    ...:     """Appends ’bar’ to the given list and returns it. 
    ...:     If target is not provided, returns [’bar’]. 
    ...:     """
    ...:     target.append("bar")
    ...:     return target
    ...: print(foo([1, 2, 3]))
    ...: print(foo())
    ...: print(foo())
[1, 2, 3, 'bar']
['bar']
['bar', 'bar']