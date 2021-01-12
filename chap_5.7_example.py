liste = [int(i) for i in input("liste des valeurs").split()]
print(liste)
"""
Dans le code suivant, l’utilisateur encode
sur une ligne, une liste de valeurs entières
séparées d’au moins un espace (par exemple 1 2 3 21 36 <return>); ces valeurs permettent d’initialiser la liste ma_liste :
"""

"""
La première ligne est équivalente à
texte = input('liste de valeurs')
ma_liste = texte.split()  # découpe le texte en parties
                          # séparées d'au moins un espace
ma_liste = [int(i) for i in ma_liste] # crée la liste
                          # en traduisant chaque partie en entier
"""
#join([i for i in s if i.isalnum()
"""
def keep_alnum_2(s):
   Nettoie s en lui retirant les caractères non alphanumériques.

    return "".join([i for i in s if i.isalnum()])
"""