import math
fact = 1
n = 0
x = float(input())
sinx = 0
while n > -1:
    if n >= 1:
        fact = (2 * n + 1) * (2 * n) * fact
    else:
        fact = 1

    inx = (-1) ** n * x ** (2 * n + 1) / fact
    sinx = sinx + inx
    if 10 ** (-6) > abs(inx):
        n = -2
    else:
        n = n + 1

print(sinx)

#  """
#  On peut calculer approximativement le sinus de x (voir définition du sinus) en effectuant la sommation des n premiers termes de la série (c'est-à-dire la somme infinie) :
#  sin(x)=x−x3/3!+x5/5!−x7/7!+...
#  où x est exprimé en radians.
#  On vous demande d'écrire un code qui lit une valeur flottante (float) x en entrée et qui imprime une approximation de sin(x).

#  Votre code additionne les termes successifs dans la série jusqu'à ce que la valeur d'un terme devienne inférieure (en valeur absolue) à une constante ϵ (prenez ϵ=10−6). Affichez (imprimé) ensuite l'approximation ainsi obtenue.

#  Attention : Calculer explicitement la valeur des factorielles peut poser des soucis lorsque vous utilisez les valeurs pour des calculs avec des float. Si c'est le cas, pensez à une autre façon de faire !

#  Votre code à tester par UpyLaB ne doit pas avoir de paramètre dans les input. Exemple : x = float(input()) plutôt que x = float(input("x = "))
#  """


""" def factorial(n):
    if n < 1:  # base case
        return 1
    else:
        result = n * factorial(n - 1)
        return result


def fibonachi(n):
    int(input("entrer sinx"))
    z = True
    While z == True:
        x = y
        x = x + fibonachi(((-1**(n+2)*x**(n+2))/(factorial(2*n+1)))
        if x-y < 10**^-6
            z=False
            return x


def sf(x):
    return (-1)**(x)


# def fib(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)

print(fib(9))

def fac(n):
    return 1 if (n < 1) else n * fac(n - 1);

n=int(input("entre un chiffre"))
print(str(n) + '! = ' + str(factorial(n)))
print(str(n) + '! = ' + str(fac(n)))
 """