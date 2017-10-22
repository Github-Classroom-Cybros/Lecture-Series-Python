from decimal import *
from fractions import Fraction
from math import floor

def getExponent(flot, exponent):
    # We need to know all significant digits that we will likely encounter
    # to gurantee maximum precision
    # 1.5 + 1.55 = 3.55  the second one had two digits of precision so we need
    # 2 digits of precision.
    # But, the way decimal is handled we need to account for the digits in the
    # interger part of the number.


    f = Fraction(flot)
    w = f
    for _ in range(exponent):
        w = w * f
    n = Context(prec=len(str(flot))).create_decimal(str(flot))
    s = str(flot)
    decimalPart = s[s.index('.')]
    getcontext().prec = len(decimalPart) * exponent + len(str(w))
    x = Decimal(1)
    # Get exponent, now with max precision taken into account
    for _ in range(exponent):
        x = x * n
    return x

print("Press 'y' to exponentiate a float fo your choice")
userChoice = input()
while userChoice == 'y' or userChoice == 'Y':
    print('Input a float you want to exponentiate: ')
    f = input()
    print("\nInput a power to raise the float by: ")
    e = input()
    print(getExponent(f,int(e)))
    print("Press 'y' to exponentiate a float fo your choice")
    userChoice = input()
