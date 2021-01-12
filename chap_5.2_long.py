import random
n = random.randint(0,100)
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
mon_tuple = (n * x1, n * y1, n * x2, n * y2)
print(mon_tuple[0])
print(mon_tuple[1])
print(mon_tuple[2]-mon_tuple[0])
print(mon_tuple[3]-mon_tuple[1])
"""
def longeur():
    mon_tuple = ((n * x1, n * y1), (n * x2, n * y2))

    dist = ((mon_tuple[0[0]] mon_tuple[0]) ** 2 + (mon_tuple[1] - mon_tuple[1]) ** 2) ** 0.5
    return print(dist)
longeur()
"""