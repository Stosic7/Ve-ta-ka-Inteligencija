def izmeni(lista):
    return {
        'pp': [x + 1 for x in lista[::2]],   # Svaki drugi od pozicije 0
        'np': [x - 1 for x in lista[1::2]]   # Svaki drugi od pozicije 1
    }

print(izmeni([8, 6, 3, 1, 1]))
