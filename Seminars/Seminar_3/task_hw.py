list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def map(funcPreobr, x):
    return funcPreobr(x)

def filter(funcFilter, x):
    return funcFilter(x)

res = []
'''
for item in list_1:
    if filter(lambda x: x % 2 != 0, item):
        res.append(map(lambda x: (x, x * x), item))
'''
res = [map(lambda x: (x, x * x), item) for item in list_1 if filter(lambda x: x % 2 != 0, item)]
print(res)
        



