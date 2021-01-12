d={'yes': 'oui', 'no':'non'}
d2= d.copy()
d2

d2['yes'] = 'OUI'
d2.clear()

from copy import deepcopy
d2 = deepcopy(d)
print(d2)

d2 = {}.fromkeys('abcde',0)
print(d2)
#assigne la valeur 0 aux clés a b c d e

print(d.get('yes',' valeur par défaut'))
#retourne la  valeur lié à la clé yes 'oui'sinon retourne le deuxième paramètre

'yes' in d #permet de vérifier que yes est une clé

d.setdefault('yes', 'Oui')    #renvoie la valeur associé déjà présente dans le dict oui
d.setdefault('three','trois') #ajoute la clé three

print(d)

d.keys()                        #renvoie les clés du dictionnaire d
d.values()                      #renvoie les valeurs du dictionnaires d
d.items()                       #renvoie les items du distionnaire

for cle, valeur in d.items():
    print(cle, valeur)

d.pop('threee','none') #supprime une clé au hasard sans paramètre
                       #supprime la clé dans le premier paramètre
                       #ne retourne pas d'erreur si second paramètre

d.update(zip('bcd', range(1,4)))
print(d)

l = [('a',1),('b',2)]
a=dict(l)             #transforme en dictionnaire

ror =dict(zip('abc',range(3)))
print(ror)