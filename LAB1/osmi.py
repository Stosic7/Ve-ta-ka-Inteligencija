from itertools import accumulate

def izmeni(lista):
    return list(accumulate(lista))

print(izmeni([1, 2, 4, 7, 9]))
