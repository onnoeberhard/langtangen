
"""
Find an approximate root of a function on a specified interval using `bisect(f, a, b, eps)`.
"""

import math

__all__ = ['bisect']

def bisect(f, a, b, eps=1e-6):
    """
    Find an approximate root of f in the interval [a, b].

    Parameters
    ----------
    f : function
        A mathematical function, defined and with root on [a, b]
    a, b : numbers
        Endpoints of the interval. a < b.
    eps : number, optional, default 1e-6
        Tolerance of error.

    Returns
    -------
    x : number
        Approximate root of f on [a, b]
    """
    if a > b:
        raise ValueError("`b` needs to be greater than `a` for the interval [a, b] to exist.")
    x = (a + b) / 2
    if abs(f(x)) < eps:
        return x
    try:
        if f(a) * f(x) < 0:
            return bisect(f, a, x, eps)
        else:
            return bisect(f, x, b, eps)
    except RecursionError as e:
        raise RecursionError(f"There seems to be no root of f on the interval [{a}, {b}]")

def test_bisect():
    """Verify `bisect` using `f` = cos(pi * x), `a` = 0 `b` = 0.82 and `eps` = 1e-12."""
    from math import cos, pi
    f = lambda x: cos(pi * x)
    a = 0
    b = 1
    eps = 1e-12
    expected = 0.5
    computed = bisect(f, a, b, eps)
    error = abs(expected - computed)
    tolerance = 1e-12
    success = error < tolerance
    msg = f"""
    Error testing `piecewise`.
    Expected:  {expected}
    Computed:  {computed}
    Error:     {error:13.6e}
    Tolerance: {tolerance:13.6e}"""
    assert success, msg

if __name__ == '__main__':
    import sys, argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", help="A mathematical function, defined and with root on [a, b]. Can include every function from the `math` module.")
    parser.add_argument('-a', type=float, default=0, help="Left endpoint of interval")
    parser.add_argument('-b', type=float, default=2, help="Right endpoint of interval")
    parser.add_argument('-eps', type=float, default=2, help="Tolerance of error")
    parser.add_argument('--test', help="Run unit test", action='store_true')
    args = parser.parse_args()
    if len(sys.argv) == 1 or args.test:
        test_bisect()
        print("All tests successfull :)")
    else:
        from math import *
        f = eval(args.f)
        root = bisect(f, args.a, args.b, args.eps)
        print(f"x = {root} is a root of {f.__name__} on [{args.a}, {args.b}]")
