import math, decimal

#chudnovsky algorithm
def calc_pi(x,places):
    decimal.getcontext().prec = places
    sum = decimal.Decimal('0.0')
    x = decimal.Decimal(x)
    while x >= 0:
        sum += (((-1)**x) * math.factorial(6*x) * (13591409 + 545140134*x))/(math.factorial(3*x)*(math.factorial(x)**3) * (640320**(3*x + decimal.Decimal(3/2))))
        x -= 1
    sum *= 12
    return (1/sum)

iterations = int(input("How Many Iterations?\n"))
places = int(input("Decimal Places?\n"))+1
print(calc_pi(iterations,places))
