def est_pair(x):
    """ Renvoie la valeur vrai si x est pair"""
    return x % 2 == 0


a = int(input("Entrez un nombre entier impair : "))
if est_pair(a):
    print("Il n'est pas impair !")