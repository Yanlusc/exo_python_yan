"""
Le problème de syracuse a ralenti les recherches durant la guerre froide, 1960.
Les soviétiques ont pensé qu'il s'agissait d'une stratégie des américains pour ralentir
la recherche scientifique.

Si le nombre est pair alors n*2
Si le nombre est impair alors n*3+1

Prouvez que la suite ne converge pas toujours vers
une suite triviale 1,4,2,1,4,2
"""

n= int(input('valeur du nombre à tester'))
while n != 1:
    if n%2 == 0 : # si le nombre entier modulo 2 vaut 0, il est pair
        n = n // 2 # //division entière ne prend pas en compte les floats
    else:
        n = 3*n+1

print(n)
