import numpy as np

p_list = [2]
p_count = 1
_guess = 3

while p_count <= 10000:

    flag = True

    for factor in p_list:
        if _guess % factor == 0:
            flag = False
            break

    if flag:
        print _guess
        p_list.append(_guess)
        p_count += 1

    _guess += 1

print p_list
print p_list.pop()
