from itertools import pairwise

def razlika(lista):
    return [x - y for x, y in pairwise(lista)]

print(razlika([8, 5, 3, 1, 1]))
