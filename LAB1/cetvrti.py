from itertools import pairwise

def zbir(lista):
    return [x + y for x, y in pairwise(lista)]

print(zbir([1, 2, 3, 4, 5])) 
