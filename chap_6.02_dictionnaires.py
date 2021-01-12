ang2fr = {'one':'un','two':'deux', 'three':'troie'}
ang2fr
#renvoie {'one':'un','two':'deux', 'three':'troie'}

ang2fr['two']
#renvoie 'deux'

""" ang2fr['five']"""
# renvoie KeyError 'five"
# la clé five n'existe pas dans le dictionnaire

d = {}

d = {'ent':1, 'list': [1,2,3], 1:'un', (1,2):3.14, 'dic'= ang2fr }
# les clés d'un dictionnaires ne doivent pas être modifiable pas de liste [], pas d'ensemble {}


d['dic']
# renvoie toute les valeurs de l'ensemble ang2fr
# soit {'one':'un','two':'deux', 'three':'troie'}

d['dic']['two']
# renvoie deux

d['list'][-1]
renvoie la dernière valeur associé à la liste soit 3

d = {'joe': 26, 'bob': 33, 'joe':36}
renvoie {'joe':36, 'bob': 33}

len()

one in ang2fr
#est-ce que la clé one appartient au dictionnaire ang2fr
# renvoie True

deux in ang2fr
#deux n'est pas une clé du dictionnaire

tel = {}
tel['Baround','Bill'] = '065-37-07-56'
tel['II','Albert'] = '02-256-89-14'

for last, first in tel:
    print(first last, tel[last, first])