def parni(lista):
    return {
        'Parni': [x for x in lista if x % 2 == 0],
        'Neparni': [x for x in lista if x % 2 != 0]
    }

print(parni([1, 7, 2, 4, 5]))
