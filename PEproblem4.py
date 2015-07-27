# Palindromes

def bool_palindrome(num):
    _numstr = str(num)
    _numlen = len(_numstr)

    for i in range(_numlen/2):
        if _numstr[i] != _numstr[_numlen - i - 1]:
            return False

    return True


def compute():
    #one number will be an 11 multiple (lets make it as large as possible)
    #other can be anything (lets reduce from max possible)
    max_pal = 0
    num1 = 990

    for num1 in range(990, 99, -11):
        for num2 in range(999, 99, -1):
            prod = num1 * num2
            if bool_palindrome(prod):
                if prod > max_pal:
                    max_pal = prod

    print max_pal


if __name__ == '__main__':
    compute()
