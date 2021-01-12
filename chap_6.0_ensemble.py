#créer un ensemble
personnages = {"rose", "serpent", "renard", "renard", "rose"}

personnages         #renvoie rose serpend renard
                    # l'ensemble supprime les doublons

len(personnages)    # renvoie 3
                    # il y a que 3 éléments dans l'ensemble

s = set('abracadabra')
s
# renvoie {'a','b','r','c','d'}

t = set('alakazam')
t
# renvoie {'a','l','k','m','z'}

s - t
# renvoie {'b','c','d','r'}

s | t
# renvoie {'a','b','c','d','l','m','k','r','z'}

s & t
# renvoie {'a'}

s.add('x')
s.remove('a')
s.discard('a') # ne fait pas d'erreur lorsque a n'est pas dans s


s |= {'t'}
# s union t
# rajoute t si pas présent dans s

s -= {'c','b','t'}
# supprime 'c', 'b', 't' de s

vide  = set()
# crée un ensemble vide

d = {}
# crée un dictionnaire

s.pop()
# enlève un élément au hasard de s

s.clear()
# supprime l'ensemble s

a = {1,2,3}
b = {1,2,3,5}
a < b
# a inclue dans b
# renvoie True a = {1 2 3} inclue dans b { 1,2,3,5}







