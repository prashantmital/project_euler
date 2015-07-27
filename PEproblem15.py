from math import factorial

# 40 total x/y increments have to be arranged
# out of which 20 are x and 20 are y

# number of ways of arranging 40 objects of which
# 20 are of 1 type and 20 are of another type

print factorial(40)/(factorial(20) * factorial(20))
