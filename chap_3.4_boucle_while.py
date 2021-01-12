Distance = 3.844e8
nombre_pliages = 0
epaisseur = 0.0001
while epaisseur < Distance:
    nombre_pliages = nombre_pliages + 1
    epaisseur = epaisseur*2

print('Nombre de pliages nécessaires:', nombre_pliages)

Distance2 = 90
Nombre_pliages2 = 0
epaisseur2 = 1

while epaisseur2 < Distance2:
    Nombre_pliages2 = Nombre_pliages2 + 1
    epaisseur2 = epaisseur2 + 1

print('le nombre de pliage2', epaisseur2)