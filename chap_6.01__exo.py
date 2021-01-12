
   mots_valides = set(mots.read().split()) # set permet de supprimer les doublons
liste_mots = list(mots_valides)            # transforme en liste
liste_mots.sort()                          # trie la liste

with open('liste_mots.txt', 'w') as res:   # Ecriture des mots
   for m in liste_mots:
       res.write(m + '\n')



