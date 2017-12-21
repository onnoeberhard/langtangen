"""
Module for computing with interest rates.
Symbols: A is present amount, A0 is initial amount,
n counts days, and p is the interest rate per year.
Given three of these parameters, the fourth can be
computed as follows:
    A  = present_amount(A0, p, n)
    A0 = initial_amount(A, p, n)
    n  = days(A0, A, p)
    p  = annual_rate(A0, A, n)
"""

__all__ = ['present_amount', 'initial_amount', 'days', 'annual_rate']

from math import log as ln

def present_amount(A0, p, n):
    return A0 * (1 + p/(360.0 * 100))**n
def initial_amount(A, p, n):
    return A * (1 + p/(360.0 * 100))**(-n)
def days(A0, A, p):
    return ln(A / A0) / ln(1 + p/(360.0 * 100))
def annual_rate(A0, A, n):
    return 360 * 100 * ((A / A0)**(1.0 / n) - 1)

if __name__ == '__main__':
    import sys
    p = float(sys.argv[1])
    years = days(1, 2, p)/365.0
    print("With p=%.2f it takes %.1f years to double" % (p, years))
