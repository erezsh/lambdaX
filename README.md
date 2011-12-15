X has two main features:

    1. It acts as an identity function ( so X(3) == 3, etc. )
    2. When performing operations on it, it returns a new class that acts as a corresponding function.

So, evaluating (X+2) will result in an instance of X, that whenever called with an argument, will return that argument plus 2. So:
    
    >>> map( X+2, [1, 2, 3] )
    [3, 4, 5]

    >>> filter( X>0, [5, -3, 2, -1, 0, 13] )
    [5, 2, 13]

    >>> l = ["oh", "brave", "new", "world"]
    >>> sorted(l,key=X[-1])
    ['world', 'brave', 'oh', 'new']

These operations can be chained:

    >>> map(2**(X+1), range(10))
    [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]

    >>> map( "P" + X[3:]*2 + "!", ["Hello", "Suzzy"] )
    ['Plolo!', 'Pzyzy!']

Some operations aren't as smooth:

    >>> map( X.upper._(), "use underscore for calling a function".split() )
    ['USE', 'UNDERSCORE', 'FOR', 'CALLING', 'A', 'FUNCTION']
    >>> filter( X.in_(range(10)), range(4,20,2))
    [4, 6, 8]

