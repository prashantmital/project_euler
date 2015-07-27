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


def compute(n_digits):
    num = 10 ** (n_digits-1)
    consec_count = 0
    while  True:
        n_distinct_factors = len(prime_factorize(num)[0])
        if n_distinct_factors >= n_digits:
            consec_count += 1
            if consec_count >= n_digits:
                print num, num-1, num-2, num-3
                break
        else:
            consec_count = 0
        num += 1
    print "Done!"

if __name__ == '__main__':
    compute(4)
