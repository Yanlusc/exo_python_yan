def symetrie_verticale(carre):
   """renvoie l'image de la matrice carre par symétrie verticale"""

   n = len(carre)
   return [[carre[i][j] for j in range(n-1,-1,-1)] for i in range(n)]

def rotation(carre):
   """renvoie l'image de la matrice carre par rotation de 90° à droite"""

   n = len(carre)
   return [[carre[i][j] for i in range(n-1,-1,-1)] for j in range(n)]

carre = [[2, 7, 6], [9, 5, 1], [4, 3, 8]]