from math import *

w = eval(input())
z=(len(w))

def plus_grand_bord(w):
    i = 0
    while i<(ceil(z/2)):
        i = i + 1
        if w[:i] == w[-i:]:
            a = w[:i]
    return(a)
print(plus_grand_bord(w))



