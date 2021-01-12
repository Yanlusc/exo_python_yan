"""
Si la valeur -1 est rencontré arrêter la moyenne
"""
a = 0
b = 0
somme = 0
while a > -1:

    a = int(input())
    if a > -1:
        somme = a + somme
        b = b + 1
    else:
        pass
moyenne = somme / b
print(moyenne)