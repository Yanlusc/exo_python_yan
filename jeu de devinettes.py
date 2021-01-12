"""
Petit jeu de devinettes version 1
"""
import random

print(" Choissisez un nombre entre 0 et 10")
secret = random.randint(0,10)
bla = int(input("Veuillez entrer le numéro choisi : "))

if bla == secret :
    print("Félicitation vous avez gasgné")
else :
    print("Le numéro gagnant était", secret, " et vous avez joué", bla)