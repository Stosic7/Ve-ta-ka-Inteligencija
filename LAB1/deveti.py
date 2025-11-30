def prosek(lista):
    return [sum(podlista) / len(podlista) for podlista in lista]

print(prosek([[1, 4, 6, 2], [4, 6, 2, 7], [3, 5], [5, 6, 2, 7]]))
