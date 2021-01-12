n = int(input('nombre de termes à calculer de la suite de Fibonacci : '))
prec = 0
succ = 1
print(prec, end = " ")
print(succ, end = " ")
for i in range(n-2):
    prec, succ = succ, prec + succ
    print(succ, end = " ")
print()
"""
Le range(n-2) est dû au fait que les 2 premiers termes ont déjà été imprimés et qu’il en reste donc n-2 à calculer.

Notons aussi l’utilisation de l’attribut end dans les print, pour imprimer les résultats sur la même ligne (avec end = " ",
chaque print est séparé par un espace), et le dernier print() permet de passer à la ligne après avoir imprimé la dernière valeur
"""