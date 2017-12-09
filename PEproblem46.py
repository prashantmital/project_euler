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


def is_prime(number):
    factors, powers = prime_factorize(number)
    if len(factors) == 1:
        return True
    else:
        return False


def list_primes_less_than_number(number):
    primes = list()
    for k in range(1, number+1):
        if is_prime(k):
            primes.append(k)
    return primes


def compute():
    number = 3
    candidate_primes = list_primes_less_than_number(number)
    flag = False
    while True:
        print("Processing {}".format(number))
        if is_prime(number):
            candidate_primes.append(number)
            number += 2
            continue
        for prime in candidate_primes:
            flag = False
            square = (number - prime)/2
            root = sqrt(square)
            if int(root) == root:
                flag = True
                break
        if flag:
            number += 2
        else:
            print("The answer is {}".format(number))
            break


if __name__ == '__main__':
    compute()
