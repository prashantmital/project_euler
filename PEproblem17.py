ONES_MAP = {  # Hundred map can be created from ones map by adding
    1: 3,     # `len('hundred')`.
    2: 3,
    3: 5,
    4: 4,
    5: 4,
    6: 3,
    7: 5,
    8: 5,
    9: 4,
}


TENS_MAP = {
    1: 3,
    2: 6,
    3: 6,
    4: 5,
    5: 5,
    6: 5,
    7: 7,
    8: 6,
    9: 6,
}


HUNDREDS_MAP = {
    idx: ONES_MAP[idx] + len('hundred') for idx in ONES_MAP.keys()
}


THOUSANDS_MAP = {
    idx: ONES_MAP[idx] + len('thousand') for idx in ONES_MAP.keys()
}


POWER10_TO_STRLEN_MAP = {
    0: ONES_MAP,
    1: TENS_MAP,
    2: HUNDREDS_MAP,
    3: THOUSANDS_MAP,
}


def digits_from_number(number_original):
    number = number_original
    power10_digits = {}
    power10 = -1
    while number != 0:
        power10 += 1
        number, digit = divmod(number, 10)
        # No need to store 0's as they don't contribute to letter count.
        if digit:
            power10_digits[power10] = digit
    return power10_digits


def number_from_digits(power10_digits):
    number = 0
    for power10, value in power10_digits.iteritems():
        number += value * pow(10, power10)
    return number


def length_from_digits(power10_digits):
    original_number = number_from_digits(power10_digits)
    length = 0
    for power10, value in power10_digits.iteritems():
        length_map = POWER10_TO_STRLEN_MAP[power10]
        length += length_map[value]
    # If number has non-zero hundreds, add length of 'and'
    # if and only if ones or tens are non-zero.
    if original_number > 100 and original_number % 100 != 0:
        length += len('and')
    return length


if __name__ == '__main__':
    total_letters = 0
    for number in range(101, 102):
        total_letters += length_from_digits(digits_from_number(number))
    print("Answer: {}".format(total_letters))
