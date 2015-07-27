from math import sqrt


def prime_factorize(num):
    factor_pow = list()
    factor_seq = list()

    count = 0
    while num % 2 == 0:
        num = num / 2
        count += 1

    if count > 0:
        factor_pow.append(count)
        factor_seq.append(2)

    for i in range(3, int(sqrt(num))+1, 2):
        count = 0

        while num % i == 0:
            num = num / i
            count += 1

        if count > 0:
            factor_pow.append(count)
            factor_seq.append(i)

    if num > 2:
        factor_pow.append(1)
        factor_seq.append(num)

    return factor_seq, factor_pow


def num_factors(factor_pow):
    count = 1
    for x in factor_pow:
        count *= (x+1)

    return count


def compute():
    n = 1

    while True:
        factor_pow = prime_factorize(n*(n+1)/2)[1]
        if num_factors(factor_pow) > 500:
            print n*(n+1)/2
            break
        else:
            n += 1

    print "Done!"

if __name__ == '__main__':
    compute()
