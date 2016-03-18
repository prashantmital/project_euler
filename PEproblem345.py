import numpy as np

_raw = """7  53 183 439 863
497 383 563  79 973
287  63 343 169 583
627 343 773 959 943
767 473 103 699 303"""

_raw_data = _raw.split('\n')
matrix = np.asarray([[float(ivar) for ivar in ovar.split()] for ovar in _raw_data])

_N = matrix.shape[0]
running_sum = 0

while _N >= 1:
    # cost is a measure of the quantity NOT ADDED to our running sum
    # essentially cost of an element is sum of the deficit caused in the running sum
    # if that element were to be chosen (subtract the element from all
    # entries on that row and col and add all these pieces to get cost)
    #        therefore it is the COST of including that element

    cost_function = np.zeros(matrix.shape)
    for row in range(_N):
        for col in range(_N):
            _score = 0
            _element = matrix[row, col]
            for loop_index in range(_N):
                _score += (matrix[row, loop_index] - _element)
                _score += (matrix[loop_index, col] - _element)
            cost_function[row, col] = _score

    # we want to minimize the cost
    # BUT we want to minimize NETT COST
    # NETTCOST is defined as the cost of selecting an element and NOT SELECTING
    # the elements on that row and column. Subtract the combined sum of costs
    # of row,column elements from the given element to arrive at this cost.

    nettcost = np.zeros(matrix.shape)
    for row in range(_N):
        for col in range(_N):
            _sum = 0
            for loop_index in range(_N):
                _sum += cost_function[row, loop_index]
                _sum += cost_function[loop_index, col]
            nettcost[row, col] = 3*cost_function[row, col] - _sum


    target_index = np.where(nettcost == nettcost.min())
    # now if multiple entries have same cost, select the entry with larger
    # magnitude so as to maximize objective function

    max_element = -1
    print len(target_index[0])
    for q in range(len(target_index[0])):
        _i, _j = target_index[0][q], target_index[1][q]
        if matrix[_i, _j] > max_element:
            max_element = matrix[_i, _j]
            i, j = _i, _j

    print "optimal element: " + str(matrix[i, j])
    running_sum += matrix[i, j]

    matrix = np.delete(matrix, (i), axis=0)
    matrix = np.delete(matrix, (j), axis=1)

    _N = _N - 1

print running_sum
