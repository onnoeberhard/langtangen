"""
A module for converting temeratures between Celsius, Fahrenheit and Kelvin.

Usage
-----
In [0]: K2C(224.1)
Out[0]: -49.04999999999998

In [1]: C2F(_)
Out[1]: -56.28999999999998

In [2]: F2K(_)
Out[2]: 224.1
"""

def C2F(T):
    return 9/5 * T + 32

def F2C(T):
    return 5/9 * (T - 32)

def C2K(T):
    return T + 273.15

def K2C(T):
    return T - 273.15

def F2K(T):
    return C2K(F2C(T))

def K2F(T):
    return C2F(K2C(T))

def test():
    """Verify all functions using `T` = 224.1K"""
    K = 224.1
    C = -49.05
    F = -56.29

    def test_func(func, in_, out):
        expected = out
        computed = func(in_)
        tolerance = 1e-12
        error = abs(expected - computed)
        success = error < tolerance
        msg = f"""
        Error testing function `{func.__name__}`.
        Expected:  {expected:13.6e}
        Computed:  {computed:13.6e}
        Error:     {error:13.6e}
        Tolerance: {tolerance:13.6e}"""
        assert success, msg

    test_func(C2F, C, F)
    test_func(F2C, F, C)
    test_func(C2K, C, K)
    test_func(K2C, K, C)
    test_func(F2K, F, K)
    test_func(K2F, K, F)

def convert(val, unit):
    if unit == 'C':
        print(f"{val}°C = %g°F = %gK" % (C2F(val), C2K(val)))
    elif unit == 'F':
        print(f"{val}°F = %g°C = %gK" % (F2C(val), F2K(val)))
    elif unit == 'K':
        print(f"{val}K = %g°C = %g°F" % (K2C(val), K2F(val)))

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        if sys.argv[1] == 'verify':
            test()
            print("All tests successful :)")
        else:
            convert(float(sys.argv[1]), sys.argv[2])
