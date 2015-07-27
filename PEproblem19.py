import numpy as np

# 1 Jan : Monday

month_len_norm_base = {'jan':31, 'feb':28, 'mar':31, 'apr':30, 'may':31, 'jun':30,
                    'jul':31, 'aug':31, 'sep':30, 'oct':31, 'nov':30, 'dec':31}

month_len_leap_base = {'jan':31, 'feb':29, 'mar':31, 'apr':30, 'may':31, 'jun':30,
                    'jul':31, 'aug':31, 'sep':30, 'oct':31, 'nov':30, 'dec':31}

def bool_leap(year):
    if year%4 == 0 and not year%100 == 0:
        return True
    elif year%400 == 0:
        return True
    else:
        return False

_ml_norm = list()
_ml_leap = list()

for m_n, m_l in zip(month_len_norm_base, month_len_leap_base):
    _ml_norm.append(month_len_norm_base[m_n])
    _ml_leap.append(month_len_leap_base[m_l])

ml_norm = np.asarray(_ml_norm, dtype=long)
ml_leap = np.asarray(_ml_leap, dtype=long)

#print ml_norm.cumsum()
#print ml_leap.cumsum()

year = 1900
sun_count = 0
cur_year = [0] * 12
cur_year[0] = -30
cur_year = np.asarray(cur_year)
seven = np.repeat(7, 12)
first = np.zeros(12)

while year <= 2000:
    cur_year[0] += 31
    if bool_leap(year):
        _month_length = ml_leap
    else:
        _month_length = ml_norm
    np.add(cur_year[1::], _month_length[:-1:], cur_year[1::])
    np.mod(cur_year, seven, first)
    sun_count += (first == 0).sum()
    year += 1

print sun_count
