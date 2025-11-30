def izbroj(lista):
    if type(lista) != list:
        return 1
    return sum(izbroj(elem) for elem in lista)

print(izbroj([1, [1, 3, [2, 4, 5, [5, 5], 4]], [2, 4], 4, 6]))
