from math import pow

# test to see how many digits in the number are possible
#for i in range(100):
#    if i <= len(str(i * 9 ** 5)):
#        print i, len(str(i * 9 ** 5))

#turns out num can be 5 or 6 digit (more likely 6 digit)

def bool_condition(num):
    _numstr = str(num)
    _sum = 0
    for digit in _numstr:
        _sum += pow(int(digit), 5)

    if _sum == num:
        return True
    else:
        return False

def compute():
    _sum = 0
    for _guess in range(2, 10**6):
        if bool_condition(_guess):
            _sum += _guess
            print _guess
    print "Sum: %d" % _sum
    print "Done"


if __name__ == '__main__':
    compute()
