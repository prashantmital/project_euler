with open("PEproblem22.txt", 'r') as _handle:
    _raw_data = _handle.readlines()[0]

data = _raw_data.split('","')
data[0] = data[0][1:]
data[-1] = data[-1][:-1]
data.sort()

list_score = list()
for index, name in enumerate(data):
    score = 0
    for letter in name:
        score += (ord(letter) - 64)
    list_score.append(score*(index+1))

print sum(list_score)
