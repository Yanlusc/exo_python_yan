#ouvre un fichier word celui-ci n'est pas dans le répertoire retourne erreur
"""mon_fichier = open("words.txt")"""

#ouvre un fichier dans un sous répertoire écrire sous window avec des slash enregistré utf-8 ou ascii

file =open("C:/Users/yanel/Desktop/Lettres de motivation/test/alphabet.txt", encoding="utf-8")
for lig in file:
    print(lig.strip())

file.close()
"""
#strip efface le carractère d'échappement

"""