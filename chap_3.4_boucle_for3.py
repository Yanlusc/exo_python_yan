# somme = 0
# for i in range(5): # fait la somme de 0 à range -1
#     somme= somme + i
# print(somme)

import functools

def sum(a, b):
    return a + b


# print(functools.reduce(sum, range(5)))
# print(functools.reduce(lambda a,b: a+b, range(5)))

dd = iter(range(5))
# print(list(dd))
print(next(dd))
print(next(dd))
print(next(dd))
print(list(dd))


def simpleGenerator():
    yield 1
    yield 2
    yield 3

for j in simpleGenerator():
    print(j)