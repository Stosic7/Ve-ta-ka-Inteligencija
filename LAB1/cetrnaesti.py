def unija(lista1, lista2):
    return lista1 + [x for x in lista2 if x not in lista1]

print(unija([5, 4, "1", "8", 7], [1, 9, "1"]))
