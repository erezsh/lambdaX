X is a composition class. It's a lambda replacement which is shorter, pickle-able, and cooler.

X has two main features:

1. It acts as an identity function ( so X(object) == object, etc. )
2. When performing operations on it, it returns a new class that acts as a corresponding function.

So, evaluating (X+2) will result in an instance of X, that whenever called with an argument, will return that argument plus 2:

    >>> map( X+2, [1, 2, 3] )
    [3, 4, 5]

    >>> pow = X**X
    >>> pow(2,8)
    256

    >>> filter( X>0, [5, -3, 2, -1, 0, 13] )
    [5, 2, 13]

    >>> l = ["oh", "brave", "new", "world"]
    >>> sorted(l,key=X[-1])
    ['world', 'brave', 'oh', 'new']

These operations can be chained and composed:

    >>> map(2**(X+1), range(10))
    [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]

    >>> sqr = X ** 2
    >>> sqr_sum = sqr + sqr
    >>> sqr_sum(3, 4)
    25

    >>> sec_per_min = 60 * X
    >>> sec_per_hour = 60 * sec_per_min
    >>> sec_per_day = 24 * sec_per_hour
    >>> sec_per_day(1)
    86400

    >>> head, tail = X[0], X[1:]
    >>> (head(tail))([1,2,3])
    2

Another feature is SameX, which is experimental (like everything here ;)

    >>> map(X**SameX, range(10))
    [1, 1, 4, 27, 256, 3125, 46656, 823543, 16777216, 387420489]

    >>> (X+SameX+SameX)('ha')
    'hahaha'

    >>> (X + ' ' + SameX[::-1])('hello!')
    'hello! !olleh'

Some operations aren't as smooth:

    >>> map( X.upper._(), "use underscore for calling a function".split() )
    ['USE', 'UNDERSCORE', 'FOR', 'CALLING', 'A', 'FUNCTION']
    >>> filter( X.in_(range(10)), range(4,20,2))
    [4, 6, 8]

## License

[MIT](http://malsup.github.com/mit-license.txt)

