a=float(input('a:'))
b=float(input('b:'))
c=float(input('c:'))

delta= b**2-4*a*c
racin= delta**0.5

if delta==0:
    print("L'équation a une racine ", -b/(2*a))
elif delta>0:
    print("L'équation a deux racines")
    print("x1 = ", (-b+racin)/(2*a))
    print("x2 = ", (b+racin)/(2*a))
else :
    print("L'équation n'a pas de solutions")
