def triple_double_lettres(mot):
   """renvoie vrai si le mot contient trois double lettres consécutives"""

   i = 0
   n = len(mot)
   res = False
   while not res and i < n - 5:
       res = mot[i] == mot[i + 1] and mot[i + 2] == mot[i + 3] \
             and mot[i + 4] == mot[i + 5]
       i += 1
   return print(res)

triple_double_lettres("rrrrhh")
#quadruple erreur