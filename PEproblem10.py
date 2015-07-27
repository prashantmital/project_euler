import numpy as np
from math import sqrt

sum = 2
p_list = [2]
p_count = 1
_guess = 3

while _guess <= 2 * 10 **6:

    flag = True

    for factor in p_list:
        if factor > _guess/2:
            break
        if _guess % factor == 0:
            flag = False
            break

    if flag:
        print _guess
        p_list.append(_guess)
        sum += _guess
        p_count += 1

    _guess += 2

print "Done!"
print sum
