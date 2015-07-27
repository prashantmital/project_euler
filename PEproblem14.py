def chain_length(num):
    count = 1
    while num != 1:
        count += 1
        if num %2 == 0:
            num = num/2
        else:
            num = 3 * num + 1

    return count

def find_max():
    max_count = 0
    max_seed = 0
    for i in xrange(10**6-1, 2, -1):
        c_len = chain_length(i)
        if c_len > max_count:
            max_count = c_len
            max_seed = i

    print max_seed

if __name__ == '__main__':
    find_max()
