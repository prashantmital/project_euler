from math import sqrt
# see question for definition of function 'd(num)'

def d(num):
    _sum = 0
    for factor in range(1, num/2+1):
        if num % factor == 0:
            _sum += factor
    return _sum

def compute(limit):
    _sum = 0
    for a in range(2, limit):
        b = d(a)
        if a == d(b) and not a == b:
            _sum += (a + b)
    return _sum/2

if __name__ == '__main__':
    amicable_sum = compute(10000)
    print amicable_sum
