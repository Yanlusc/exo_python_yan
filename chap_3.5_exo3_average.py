"""
Si la valeur -1 est rencontrée arrêter la moyenne
"""

a = int(input('entrer un numero '))
 
# while a > -1:  
#     if a > -1:
#         print(a)
#         somme = a + somme
#         b = b + 1
#         a = a-1
#     else:
#         # calcule qui prends du temps
#         pass

results = range(0, (a + 1))
moyenne = sum(x for x in results) / (a + 1)

    
# print("result = " + str(somme))
# print("b = " + str(b))
# moyenne =  somme/ b
print(moyenne)

# def doSomething(n):
#     pass # TODO: do something here next monday