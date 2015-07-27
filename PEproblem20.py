from math import factorial

_raw = str(factorial(100))

_sum = 0

for x in _raw:
    _sum += int(x)

print _sum
