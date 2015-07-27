_raw = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""

_raw_data = _raw.split('\n')
data = [[int(ivar) for ivar in ovar.split()] for ovar in _raw_data]

normalized_data = [[float(ivar)/max(ovar) for ivar in ovar] for ovar in data]

pos = 0
path = [0]
level = 0

while len(path) < len(data):
    left = normalized_data[level + 1][pos]
    right = normalized_data[level + 1][pos + 1]
    if left > right:
        path.append(pos)
        level += 1
    else:
        pos += 1
        path.append(pos)
        level += 1


path_sum = 0

for row_index, col_index in enumerate(path):
    path_sum += data[row_index][col_index]

print path_sum
