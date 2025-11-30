def presek(lista1, lista2):
    return list(x for x in lista1 if x in lista2)

print(presek([5, 4, "1", "8", 3, 7], [1, 9, "1"]))
