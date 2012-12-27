from x import X

def _test_getattr_and_call():
    assert X.upper._()('hello') == 'HELLO'
    assert X.zfill._(3)('7') == '007'
    print( "getattr and call OK!" )

def _test_slice():
    head, tail = X[0], X[1:]
    l = [1,2,3,4]
    assert head(l) == 1
    assert tail(l) == [2,3,4]
    print( "Slice OK!" )

def _test_pickle():
    import pickle
    expr = 1 + (X + 3) * 4
    assert expr(5) == 33

    s = pickle.dumps(expr, 0)
    expr2 = pickle.loads(s)
    res = expr2(5)
    assert res == 33

    s = pickle.dumps(expr, 1)
    expr2 = pickle.loads(s)
    res = expr2(5)
    assert res == 33

    s = pickle.dumps(expr, 2)
    expr2 = pickle.loads(s)
    res = expr2(5)
    assert res == 33

    print( "Pickle OK!" )

def _test_hash():
    assert hash(X+1) == hash(X+1)
    assert hash(X._(X)) == hash(X._(X))
    print( "Hash OK!" )

def _test_multiple_args():
    g = X + 2*X
    assert g(3,5) == g(3)(5) == 13
    assert g(5,3) == g(5)(3) == 11
    g = 2*X + X
    assert g(3,5) == g(3)(5) == 11
    assert g(5,3) == g(5)(3) == 13
    print( "Multiple args OK!" )

def _test_composition():
    f = X**2 - 1
    g = f + 2*f
    assert g(3,5) == 56

    h = g - f + 2
    assert h(1,2,3) == 0


def _test():
    _test_getattr_and_call()
    _test_pickle()
    _test_hash()
    _test_slice()
    _test_multiple_args()
    _test_composition()

if __name__ == '__main__':
    _test()

