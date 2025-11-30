def brojel(*args):
    return [len(x) if type(x) == list else -1 for x in args]

print(brojel([1, 2], [3, 4, 5], 'el', ['1', 1]))
