"""
Petit jeu de devinette version 1
"""
import random

print(" Choissisez un nombre entre 0 et 10")
secret = random.randint(0,10)
number = int(input("Veuillez entrer le numéro choisi : "))
If number = secret :
    print("Félicitation vous avez gangné")
else :
    print("Le numéro gagnant était", secret, " et vous avez joué", number)