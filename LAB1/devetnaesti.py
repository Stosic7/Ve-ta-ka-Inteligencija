from functools import reduce

def stepenuj(lista):
    return [reduce(lambda x, y: x ** y, t) for t in lista]

print(stepenuj([(1, 4, 2), (2, 5, 1), (2, 2, 2, 2), (5, )]))
