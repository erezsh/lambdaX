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

def _test():
    _test_getattr_and_call()
    _test_pickle()
    _test_hash()
    _test_slice()

if __name__ == '__main__':
    _test()

