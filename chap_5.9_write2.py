#lis un fichier et enregistre les données dans un
#autre fichier en supprimant les données


f_in = input("fichier de données: ")
f_out= input("fichier de résultat: ")
with open(f_out, 'w', encoding='utf-8') as r:
    deja_vu = set({})
    for text in open(f_in, encoding='utf-8'):
        if text not in deja_vu:
            deja_vu ={text}|deja_vu
            r.write(text)
"""
Le module Python os peut être utile pour cela en permettant avec la fonction chdir, de changer le répertoire courant.
"""

"""
import os
os.chdir('Users/tmassart/Python/scripts')
"""
"""

f = open("name", "a" or "w" "r")
a permet de préserver les données déjà présentes
r par défaut read
w write

f.read()            #retourne le contenu du fichier
f.readline()        lit une ligne
f.readlines()       lit toutes les lignes du fichiers
f.write(Bonjour)    écrit bonjour dans le fichier f
f.close()           ferme le fichier f

"""