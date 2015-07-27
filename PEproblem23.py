from sys import argv

def sum_of_factors(num):
    _sum = 0
    for factor in range(1, num/2+1):
        if num % factor == 0:
            _sum += factor
    return _sum

for i in range(int(argv[1])):
    if sum_of_factors(i) > i:
        print i
