from math import sqrt
from numpy import roots

# choose a c
# get a generator expression for a and b
# print results

for c in range(5, 997):
    x = 5 * 10**5 - c * 10**3
    y = 1000 - c
    solution = roots([1, -y, x])
    if solution[0].imag == 0:
        a, b = (solution[0].real, solution[1].real)
        if a + b + c == 1000 and (a%1 == 0 and a > 0):
            print a, b, c
            print a*b*c
            print a**2 + b**2 == c**2
