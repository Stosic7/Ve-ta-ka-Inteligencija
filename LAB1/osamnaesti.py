from itertools import pairwise

def kreiraj(lista):
    return [[x for x in p1 if x not in p2] for p1, p2 in pairwise(lista)]

print(kreiraj([[1, 2, 3], [2, 4, 5], [4, 5, 6, 7], [1, 5]]))
