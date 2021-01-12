n = int(input('borne supérieur à ne pas dépasser pour calculer la suite de Fibonacci : '))
prec = 0
succ = 1
print(prec, end = " ")
while succ < n :
    print(succ, end = " ")
    prec, succ = succ, prec + succ
print()

"""
Notons qu’ici en plus d’utiliser un while, succ est imprimé juste après le test (condition de continuation du while) pour s’assurer qu’il faut effectivement l’imprimer.

Le programmeur devra toujours essayer d’avoir non seulement un code correct pour toutes les exécutions possibles, mais également le plus efficace possible tout en étant le plus clair possible. Nous reviendrons sur cet aspect plus tard.

Note : une instruction for peut en général facilement est traduisible par un while même si cela donne du code plus compliqué et donc moins lisible; c’est donc à déconseillé.
"""